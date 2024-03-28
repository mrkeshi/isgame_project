from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView

from Post.models import Articles,ArticleCategories


def CategoryPage(request,title):
    if(title):
        if(ArticleCategories.objects.filter(title=title).first()==None):
            return Handler404(request)
        page: int = 1
        if (request.GET.get('page')):
            page: int = request.GET.get('page')
        myArticles = Articles.objects.filter(is_active=True)
        myArticles.filter(title=title)

        paginator = Paginator(myArticles.order_by('-is_pin', '-created_date'), 10)
        myArticles = paginator.page(page)

        return render(request,'Home/CategoryPage.html',{
            "articles": myArticles,
            'paginator': paginator,
            'title':title
        })
    else:
        return Handler404(request)

def Handler404(request, template_name='OtherPage/404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response


def Blog(request):
    pass