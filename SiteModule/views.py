from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import FormView, UpdateView, ListView
from django.urls import reverse

from SiteModule.forms import AddSocialForm,SettingForm
from SiteModule.models import SocialMediaLink,PublicSettings
from User.forms import SocialLinkForm
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


def Manage_Settings(request):
    print(PublicSettings.objects.first())
    form1 = SettingForm(instance=PublicSettings.objects.first())
    social_link_instance =SocialMediaLink.objects.filter(user=None).first()
    form2=SocialLinkForm(instance=social_link_instance)
    if (request.method == "POST"):
        form1 = SettingForm(request.POST, request.FILES, instance=PublicSettings.objects.first())
        form2 = SocialLinkForm(request.POST,instance=social_link_instance)
        if (form1.is_valid() and form2.is_valid()):
            form2.save()
            form1.save()
        return redirect(reverse('manage_settings'))
    else:
        return render(request,'Settings/Setting.html',{
            'form1':form1,
             'form2':form2
        })

