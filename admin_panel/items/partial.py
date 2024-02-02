from django.shortcuts import render
from User.models import User
from SiteModule.models import PublicSettings
from Contact.models import Contact
def header_component(request):
    user=request.user
    return  render(request, './component/header_component.html', {
        'site':PublicSettings.objects.first(),
        'contact':Contact.objects.filter(is_Displayed=False).all()
    })
def aside_component(request):
    user = request.user
    return  render(request, 'component/sidebar_component.html',{
        'user': user
    })