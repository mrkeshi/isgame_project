from django.shortcuts import render
from Post.models import ArticleCategories

def CategoryBox(request):
    cat=ArticleCategories.objects.order_by('id')
    return render(request,"HomeComponent/CategoryComponent.html",{
        'items':cat,
    })