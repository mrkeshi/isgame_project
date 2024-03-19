from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView,TemplateView
from .forms import LoginForm,RegisterForm
from User import models
from django.contrib import messages

# Create your views here.
class RegisterUser(FormView):
    template_name = 'UserProfile/register.html'
    form_class = RegisterForm
    def form_valid(self, form):
        newuser = models.User(first_name=form.cleaned_data.get('first_name'),
                              email=form.cleaned_data.get('email'),
                              username=form.cleaned_data.get('email').split('@')[0]
                              )
        newuser.set_password(form.cleaned_data.get('password'))
        newuser.save()
        if (newuser.id):
            messages.success(self.request,
                             "یوزر شما با موفقیت ثبت شد، لطفا جهت فعالسازی حساب کاربری خود وارد ایمیل شوید.")
        return redirect(self.request.META.get('HTTP_REFERER'))
        # return super().form_valid(form)
class LoginUser(FormView):
    template_name = 'UserProfile/login.html'
    form_class = LoginForm
    def form_valid(self, form):
        user: models.User = form.cleaned_data.get('username')
        if user is not None:
            if not user.check_password(form.cleaned_data.get('password')):
                return redirect(self.request.META.get('HTTP_REFERER'))
        else:
            messages.success(self.request,"ثبت نام با موفقیت انجام شد")
            return redirect(self.request.META.get('HTTP_REFERER'))
        login(self.request, user)
        return redirect(reverse_lazy('UserProfile'))

class UserProfile(TemplateView):
    template_name = "UserProfile/UserProfile.html"
