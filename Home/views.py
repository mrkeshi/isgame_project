from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView

from Menu.models import Menu
from Post.models import Articles,ArticleCategories


# Create your views here.
def HomePage(request):
    page: int = 1
    if (request.GET.get('page')):
        page: int = request.GET.get('page')
    myArticles = Articles.objects.filter(is_active=True).order_by('-is_pin','-created_date')
    paginator = Paginator(myArticles, 10)
    myArticles = paginator.page(page)
    return render(request, 'Home/index.html', {
        "articles":myArticles,
        'paginator': paginator

    })


def HeaderOne(request):
    Objects = Menu.objects.filter(place_menu="MN1",is_active=True).all()

    return render(request, 'layout/HomeLayout/HomeComponent/header1.html', {
        'menus': Objects
    })

class CategoryPage(DetailView):
    model = ArticleCategories
    template_name = 'HomeComponent/footer1.html'