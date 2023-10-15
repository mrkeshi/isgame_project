from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, TemplateView
from django.utils.crypto import get_random_string
from django.http import HttpResponse

from utils.Email_Service import Email
from utils.Http_service import get_client_ip
from . import forms, models
from django.contrib import messages
from .models import incorrect_attempts, TokenAuth, User
from django.utils import timezone
from datetime import timedelta
import time


def Check_Attempt(user):
    Attmpt = len(
        incorrect_attempts.objects.filter(user=user, is_ness=True, date__gte=timezone.now() - timedelta(86400)))

    if Attmpt >= 5:
        return True
    return False


def Add_Attempt(user, status, request):
    if (status == 0):
        At = incorrect_attempts(user=user, ip=get_client_ip(request), browser=request.user_agent.browser.family,
                                device=request.user_agent.os.family)
    else:
        At = incorrect_attempts(user=user, ip=get_client_ip(request), is_ness=False, is_login=True,
                                browser=request.user_agent.browser.family, device=request.user_agent.os.family)
        ax = incorrect_attempts.objects.filter(user_id=user.id).update(is_ness=False)

    At.save()


class auth_admin_register(FormView):
    template_name = 'Auth/register.html'
    form_class = forms.RegisterForm

    def form_valid(self, form):
        newuser = models.User(first_name=form.cleaned_data.get('first_name'),
                              last_name=form.cleaned_data.get('last_name'),
                              email=form.cleaned_data.get('email'),
                              username=form.cleaned_data.get('username'),
                              )
        newuser.set_password(form.cleaned_data.get('password'))
        newuser.save()
        if (newuser.id):
            messages.success(self.request,
                             "یوزر شما با موفقیت ثبت شد، لطفا جهت فعالسازی حساب کاربری خود وارد ایمیل شوید.")
        return redirect(self.request.META.get('HTTP_REFERER'))
        # return super().form_valid(form)


class auth_admin_login(FormView):
    template_name = 'Auth/login.html'
    form_class = forms.LoginForm

    def form_valid(self, form):
        user: models.User = form.cleaned_data.get('username')
        if user is not None:
            if Check_Attempt(user):
                messages.error(self.request, "بدلیل تلاش زیاد ورود شما قفل شده است.")
                return redirect(self.request.META.get('HTTP_REFERER'))
            if not user.check_password(form.cleaned_data.get('password')):
                Add_Attempt(user, 0, self.request)
                messages.error(self.request, "نام کاربری با رمز عبور مطابقت ندارد")
                return redirect(self.request.META.get('HTTP_REFERER'))
        else:
            messages.error(self.request, "نام کاربری با رمز عبور مطابقت ندارد")
            return redirect(self.request.META.get('HTTP_REFERER'))

        login(self.request, user)
        Add_Attempt(user, 1, self.request)
        return redirect(reverse_lazy('dashboard'))

    def form_invalid(self, form):
        messages.error(self.request, 'نام کاربری با رمز عبور مطابقت ندارد')
        return super(auth_admin_login, self).form_invalid(form)


class User_sissions(ListView):
    model = incorrect_attempts
    paginate_by = 10
    template_name = 'User_Sission.html'

    def get_queryset(self):
        query = super(User_sissions, self).get_queryset()
        query = query.filter(user=self.request.user).order_by('-date')
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(User_sissions, self).get_context_data(**kwargs)
        data['none_delete'] = incorrect_attempts.objects.filter(user=self.request.user).order_by('-date').first().id
        return data


def Delete_session(request, pk):
    item = incorrect_attempts.objects.filter(id=pk).first()
    if (item is not None and item.id != incorrect_attempts.objects.order_by('-date').first().id):
        item.delete()
    else:
        pass
        # Todo: send message
    return redirect(request.META.get('HTTP_REFERER'))


def mylogout(request):
    if (request.user.is_authenticated):
        logout(request)
        messages.success(request, "شما با موفقیت خارج شدید")
    else:
        messages.error(request, 'کصکش شما لاگین نکردی!')
    return redirect(reverse('admin_login'))


class ResetPassword(FormView):
    template_name = 'Auth/resetpassword.html'
    form_class = forms.ResetPassword
    success_url = reverse_lazy('admin_login')

    def form_valid(self, form):
        dat = super(ResetPassword, self).form_valid(form)
        token = get_random_string(76)
        user: models.User = form.cleaned_data.get('username')
        user.tokenauth_set.all().delete()
        user.tokenauth_set.create(token=token)
        user.save()
        Email('بازیابی پسورد', form.cleaned_data.get('username').email, {
            'name': form.cleaned_data.get('username').first_name,
            'link': token,
            'btnname': 'بازنشانی پسورد',
            'text': ' این ایمیل جهت بازیابی پسورد شما ارسال شده است و تا 24 ساعت دیگر معتبر است . لطفا جهت بازیابی حساب بر روی این  دکمه زیر کلیک کنید.'
        }, 'sendemail.html')
        messages.success(self.request, "ایمیل بازیابی پسورد با موفقیت برای شما ارسال شد")
        return dat

    def form_invalid(self, form):
        messages.error(self.request, "خطا چنین کاربری یافت نشد")
        return super(ResetPassword, self).form_invalid(form)


class ResetPasswordConfirm(FormView):
    template_name = 'Auth/confirm_resetpassword.html'
    form_class = forms.ResetPasswordConfirm
    success_url = reverse_lazy('admin_login')

    def get(self, request, *args, **kwargs):
        content = super(ResetPasswordConfirm, self).get(request, args, kwargs)
        token = self.kwargs.get('token')
        row = TokenAuth.objects.filter(token=token, date__gte=timezone.now() - timedelta(86400)).first()
        if row is None:
            messages.error(self.request, 'توکن وارد شده نامعتبر می باشد لطفا دوباره چک کنید')
            return redirect(reverse('admin_login'))
        return content

    def get_context_data(self, **kwargs):
        data = super(ResetPasswordConfirm, self).get_context_data()
        data['token'] = self.kwargs.get('token')
        return data

    def form_valid(self, form):
        user = User.objects.filter(tokenauth__token=self.kwargs.get('token')).first()
        user.set_password(form.cleaned_data.get('confirm_password'))
        user.save()
        user.tokenauth_set.all().delete()
        user.incorrect_attempts_set.update(is_ness=False)

        messages.success(self.request, 'رمز عبور شما با موفقیت تغییر کرد.')
        return super(ResetPasswordConfirm, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'رمز عبور با تکرار رمز عبور مطابقت ندارد.')
        return super(ResetPasswordConfirm, self).form_invalid(form)


def Profile(request):
    return render(request,'User/Profile.html',{})
    # formUser=

def index(request):
    return  HttpResponse('<h1>hellow world</h1>')