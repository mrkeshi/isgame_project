from django.shortcuts import render

from Menu.models import Menu
from Post.models import Articles


# Create your views here.
def HomePage(request):
    post=Articles.objects.filter(is_active=True)
    return render(request, 'Home/index.html', {
        "articles":post,

    })


def HeaderOne(request):
    Objects = Menu.objects.filter(place_menu="MN1",is_active=True).all()

    return render(request, 'layout/HomeLayout/HomeComponent/header1.html', {
        'menus': Objects
    })
