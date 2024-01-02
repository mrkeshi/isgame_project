from django.contrib import messages
from django.db.models import Count, F
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import FormView, UpdateView, ListView
from django.views import View
# Create your views here.
from django.views.generic.detail import BaseDetailView

from SiteModule.forms import AddSocialForm
from SiteModule.models import SocialMediaLink


class addSocialLink(FormView):
    template_name = 'Social/addSocialLink.html'
    success_url = reverse_lazy('social_link')
    form_class = AddSocialForm

    def get_context_data(self, **kwargs):
        data = super(addSocialLink, self).get_context_data()
        data['user'] = self.request.user.username
        return data


    def form_valid(self, form):
        if(self.request.POST.get('myuser')!= '1' and not form.cleaned_data.get('is_setting') ):
            messages.error(self.request,"لطفا مشخص کنید که این تنظیمات مربوط به کدام قسمت است.(یکی از فیلد های issetting یا user را تکمیل کنید.)")
            return self.form_invalid(form)
        if(SocialMediaLink.objects.filter(user=self.request.user).first() and self.request.POST.get('myuser')== '1'):
            messages.error(self.request,
                           "این تنظیمات از قبل برای این یوزر ذخیره شده است")
            return self.form_invalid(form)

        data=form.save(commit=False)
        if(self.request.POST.get('my!user')=='1'):
            data.user=self.request.user
        data.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        print("form is not valid")
        return super(addSocialLink, self).form_invalid(form)


class SocialLinks(ListView):
    model = SocialMediaLink
    template_name = 'Social/ListSocialLink.html'
    context_object_name = 'data'

class EditSocialItem(UpdateView):
    template_name = 'Social/editSocialLink.html'
    success_url = reverse_lazy('social_link')
    form_class = AddSocialForm
    context_object_name = 'data'
    def get_object(self, *args, **kwargs):
        social = get_object_or_404(SocialMediaLink, pk=self.kwargs['id'])
        return social

    def get_context_data(self, **kwargs):

        data = super(EditSocialItem, self).get_context_data(**kwargs)

        return data


def delete_item(request, id):
    item = SocialMediaLink.objects.filter(id=id).first()
    if (item is not None):
        item.delete()
    else:
        pass
        # Todo: send message
    return redirect(request.META.get('HTTP_REFERER'))


def Manage_Settings(requst):

    return render(requst,"Settings/Setting.html",{})