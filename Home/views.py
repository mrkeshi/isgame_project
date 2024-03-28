from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from Menu.models import Menu
from Post.models import Articles, ArticleCategories
from SiteModule.models import Widget


# Create your views here.
def HomePage(request):
    page: int = 1
    if (request.GET.get('page')):
        page: int = request.GET.get('page')
    myArticles = Articles.objects.filter(is_active=True).order_by('-is_pin', '-created_date')
    paginator = Paginator(myArticles, 10)
    myArticles = paginator.page(page)
    return render(request, 'Home/index.html', {
        "articles": myArticles,
        'paginator': paginator,
        'widget': Widget.objects.first()

    })


def HeaderOne(request):
    Objects = Menu.objects.filter(place_menu="MN1", is_active=True).all()

    return render(request, 'layout/HomeLayout/HomeComponent/header1.html', {
        'menus': Objects
    })


def HeaderTwo(request):
    Objects = Menu.objects.filter(place_menu="MN2", is_active=True).all()
    return render(request, 'layout/HomeLayout/HomeComponent/header2.html', {
        'menus': Objects
    })

def HeaderTree(request):
    Objects = Menu.objects.filter(place_menu="MN3", is_active=True).all()
    return render(request, 'layout/HomeLayout/HomeComponent/header3.html', {
        'menus': Objects
    })

def FooterOne(request):
    return render(request, 'layout/HomeLayout/HomeComponent/footer1.html', {

    })


def FooterOne(request):
    menus = Menu.objects.filter(place_menu="FN1", is_active=True)
    categories = ArticleCategories.objects.order_by('id')[:5]
    articles = Articles.objects.filter(is_pin=True).order_by('-id')[:5]
    return render(request, 'layout/HomeLayout/HomeComponent/footer1.html', {
        'menus': menus,
        'categories': categories,
        'articles': articles
    })


def FooterTwo(request):
    menus = Menu.objects.filter(place_menu="FN1", is_active=True)
    return render(request, 'layout/HomeLayout/HomeComponent/footer2.html', {
        'menus': menus
    })


# component
class CategoryPage(DetailView):
    model = ArticleCategories
    template_name = 'HomeComponent/footer1.html'


class SinglePost(DetailView):
    model = Articles
    slug_field = 'title'
    template_name = 'Home/singlePost.html'
    context_object_name = 'post'
    # def get_context_data(self, **kwargs):
    #     con=super().get_context_data(**kwargs)
    #     print("--------------------------------------------------------")
    #     print(con.categories.all())
    #     print("-------------------------------------------------------")
    #     return con


def Category(request, title):
    return HttpResponse(title)


class TagPage(DetailView):
    pass
