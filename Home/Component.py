from django.shortcuts import render
from Post.models import ArticleCategories

def CategoryBox(request):
    cat=ArticleCategories.objects.order_by('id')
    # comments=Comment.objects.all()

    return render(request,"HomeComponent/CategoryComponent.html",{
        'items':cat,
    })
# def AdsBanner(request)