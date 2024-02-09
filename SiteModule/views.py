from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import FormView, UpdateView, ListView, TemplateView
from django.urls import reverse

from SiteModule.forms import AddSocialForm,SettingForm,GalleryForm
from SiteModule.models import SocialMediaLink,PublicSettings
from User.forms import SocialLinkForm
from .models import MediaGallery
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
        if(self.request.POST.get('myuser')=='1'):
            data.user=self.request.user
        data.save()

        return super().form_valid(form)

    def form_invalid(self, form):

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
    public_settings_instance = PublicSettings.objects.first()
    social_link_instance = SocialMediaLink.objects.filter(user=None).first()

    form1 = SettingForm(instance=public_settings_instance)
    form2 = SocialLinkForm(instance=social_link_instance)

    if request.method == "POST":
        form1 = SettingForm(request.POST, request.FILES, instance=public_settings_instance)
        form2 = SocialLinkForm(request.POST, instance=social_link_instance)

        if form1.is_valid() and form2.is_valid():
            form2.save()
            form1.save()
            messages.success(request, 'تنظیمات با موفقیت بروزرسانی شد')
            return redirect(reverse('manage_settings'))

    context = {
        'form1': form1,
        'form2': form2,
        'logos': PublicSettings.objects.only('logoSite', 'logoIcon').first(),
    }

    return render(request, 'Settings/Setting.html', context)

# Gallery
def Add(request):
    form = GalleryForm(request.POST or None, request.FILES or None)
    if request.is_ajax():
        if form.is_valid():

            form.save()
            return JsonResponse(
                {'status':True,
                 'message':'تصویر با موفقیت آپلود شد!'
                 }
            )
        else:
            return JsonResponse(
                {'status': False,
                 'message':'خطا در آپلود فایل. لطفا مجددا امتحان فرمایید',
                 }
            )
    context = {
        'form': form,
    }
    print(form)
    return render(request, "Gallery/add.html",context)

#gallery index
class GalleryMange(TemplateView):
    template_name = "Gallery/index.html"
def GalleryPage(request):
    page: int = 1
    if (request.GET.get('page')):
        page: int = request.GET.get('page')
    Gallery = MediaGallery.objects.order_by('-id')
    paginator = Paginator(Gallery, 40)
    Gallery = paginator.page(page)

    return render(request,"Gallery/items.html",{
        'paginator': paginator,
        'items': Gallery,
    })


def DeletedItems (request):
    if request.method == 'POST':
        ids=request.POST.getlist('keys[]')
        try:
            selects=MediaGallery.objects.filter(id__in=ids)
            count=selects.count()
            return JsonResponse({
                'status':True,
                'count':count,
                'result':GalleryPage(request).content.decode('utf-8')
            })
        except:
            return JsonResponse({
                'status': False})
