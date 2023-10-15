from django.shortcuts import render
from User.models import User
def header_component(request):
    user=request.user
    return  render(request, './component/header_component.html', {
        'user':user
    })
def aside_component(request):
    user = request.user
    return  render(request, 'component/sidebar_component.html',{
        'user': user
    })