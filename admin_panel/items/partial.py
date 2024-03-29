from django.shortcuts import render
from User.models import User, incorrect_attempts
from SiteModule.models import PublicSettings
from Contact.models import Contact
from Comment.models import Comment
def header_component(request):
    user = request.user
    con=Contact.objects.filter(is_Displayed=False).count()
    att=incorrect_attempts.objects.filter(user=user,is_checked=False).count()

    return  render(request, './component/header_component.html', {
        'site':PublicSettings.objects.first(),
        'contact':con,
        'attempt':att,
        'res':att+con
    })
def aside_component(request):
    user = request.user
    return  render(request, 'component/sidebar_component.html',{
        'user': user,
        'CommentCount':Comment.objects.filter(active=False).count
    })
def siteName(request):
    return