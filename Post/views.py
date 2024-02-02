from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView, DeleteView, UpdateView

from Post.forms import AddTagForm, AddCategoryForm, AddArticleForm
from Post.models import ArticleTags, ArticleCategories, Articles
from django.utils.text import slugify
from django.core.paginator import Paginator


# اhelper function

def FindOrCreateTag(tags):
    item = []
    for tag in tags:
        obj = ArticleTags.objects.get_or_create(title=tag, defaults={'title': tag, 'url': slugify(tag,allow_unicode=True)})
        item.append(obj[0].id)
    return item

    # main function


class PostManger(TemplateView):
    template_name = 'Post/ListPost.html'


def ListPost(request):
    page: int = 1
    if (request.GET.get('page')):
        page: int = request.GET.get('page')
    myArticles = Articles.objects.order_by('-id')

    if (request.POST.get('title')):
        myArticles = myArticles.filter(title__icontains=request.POST.get('title')).all()

    paginator = Paginator(myArticles, 5)
    myArticles = paginator.page(page)

    return render(request, 'Post/includes/ListPostsComponents.html', {
        'Articles': myArticles,
        'cats': ArticleCategories.objects.annotate(num_article_count=Count('articles')).filter(num_article_count__gt=0),
        'times': Articles.objects.all().annotate(date=TruncMonth('created_date')).values('date').annotate(
            count=Count('id')).order_by('-date'),
        'paginator': paginator
    })


class TagManer(ListView):
    template_name = 'Post/listTag.html'
    model = ArticleTags
    context_object_name = 'data'


class CategoryManger(ListView):
    template_name = 'Post/listCategory.html'
    model = ArticleCategories
    context_object_name = 'data'


class PostAdd(FormView):
    template_name = 'Post/addPost.html'
    form_class = AddArticleForm
    success_url = reverse_lazy('post_admin')

    def form_valid(self, form):

        thought = form.save(commit=False)
        thought.author = self.request.user
        thought.save()
        if (form.cleaned_data.get('mytag').strip() != ''):
            tags: str = form.cleaned_data.get('mytag')
            Rtags = FindOrCreateTag(tags.strip().split(';'))
            thought.tags.set(Rtags)
        if (form.cleaned_data.get('categories') != ''):
            thought.categories.set(form.cleaned_data.get('categories'))
        return super(PostAdd, self).form_valid(form)


class TagAdd(FormView):
    form_class = AddTagForm
    template_name = 'Post/addTag.html'
    success_url = reverse_lazy('tag_admin')

    def form_valid(self, form):
        form.save()
        return super(TagAdd, self).form_valid(form)


class CategoryAdd(FormView):
    form_class = AddCategoryForm
    template_name = 'Post/addCategory.html'
    success_url = reverse_lazy('category_admin')

    def form_valid(self, form):
        super(CategoryAdd, self).form_valid(form)
        form.save()


def PostDelete(request):
    if request.method == 'POST':
        id = (request.POST.getlist('id[]'))

        deleteditem = Articles.objects.filter(id__in=id)

        try:
            if (deleteditem.count() > 0):
                print(deleteditem.values_list('id', flat=True).all())
                print('true')
                # row = deleteditem.delete()
                return JsonResponse({
                    'status': True,
                    'ids': list(deleteditem.values_list('id', flat=True).all())
                })

            else:
                raise ValueError('nothing item dont delted')
        except:
            return JsonResponse({
                'status': False})


class TagDelete(DeleteView):
    template_name = 'Post/listTag.html'
    model = ArticleTags
    success_url = reverse_lazy('tag_admin')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class CategoryDelete(DeleteView):
    template_name = 'Post/listCategory.html'
    model = ArticleCategories
    success_url = reverse_lazy('category_admin')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class EditPost(FormView):
    pass


class EditTag(UpdateView):
    template_name = 'Post/editTag.html'
    success_url = reverse_lazy('tag_admin')
    form_class = AddTagForm

    def get_object(self, *args, **kwargs):
        tag = get_object_or_404(ArticleTags, pk=self.kwargs['id'])
        return tag


class EditCategory(UpdateView):
    template_name = 'Post/editCategory.html'
    success_url = reverse_lazy('category_admin')
    form_class = AddCategoryForm

    def get_object(self, *args, **kwargs):
        cat = get_object_or_404(ArticleCategories, pk=self.kwargs['id'])
        return cat
