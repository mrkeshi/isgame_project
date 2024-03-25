from datetime import datetime, timedelta

from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView, DeleteView, UpdateView

from Post.forms import AddTagForm, AddCategoryForm, AddArticleForm,DownloadBoxForm
from Post.models import ArticleTags, ArticleCategories, Articles,DownloadBox
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.contrib import messages


# اhelper function

def FindOrCreateTag(tags):

    item = []
    for tag in tags:
        obj= ArticleTags.objects.get_or_create(title=tag)

        item.append(obj[0].id)
    return item

    # main function


class PostManger(TemplateView):
    template_name = 'Post/ListPost.html'
    def get_context_data(self, **kwargs):
        myarticles:Articles=None
        con=super().get_context_data(**kwargs)
        con['cats']= ArticleCategories.objects.annotate(num_article_count=Count('articles')).filter(num_article_count__gt=0)
        con['times']=Articles.objects.all().annotate(date=TruncMonth('created_date')).values('date').annotate(
            count=Count('id')).order_by('-date')
        return con

def ListPost(request):
    myArticles: Articles = None
    page: int = 1
    if (request.GET.get('page')):
        page: int = request.GET.get('page')
    myArticles = Articles.objects
    if (request.GET.get('title')):
        if(request.GET.get('title')!="all"):
            myArticles=myArticles.filter(title__icontains=request.GET.get('title'))

    if(request.GET.get('category')):

        if (request.GET.get('category') != "all"):
            myArticles=myArticles.filter(categories__id=request.GET.get('category'))

    if(request.GET.get('date')):
        if(request.GET.get('date')!='all'):
            ti=request.GET.get('date')
            start = datetime.strptime(ti, '%Y%m%d')
            next_month_start = (start.replace(day=28) + timedelta(days=4))
            myArticles=Articles.objects.filter(created_date__range=(start, next_month_start))

    paginator = Paginator(myArticles.all().order_by('-id'), 10)
    myArticles = paginator.page(page)

    return render(request, 'Post/includes/ListPostsComponents.html', {
        'Articles': myArticles,
        'paginator': paginator
    })


class TagManer(ListView):
    template_name = 'Post/listTag.html'
    model = ArticleTags
    context_object_name = 'data'
    paginate_by = 10

class CategoryManger(ListView):
    template_name = 'Post/listCategory.html'
    model = ArticleCategories
    context_object_name = 'data'

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

        form.save()
        return      super(CategoryAdd, self).form_valid(form)

def PostDelete(request):
    if request.method == 'POST':
        id = (request.POST.getlist('id[]'))

        deleteditem = Articles.objects.filter(id__in=id)

        try:
            if (deleteditem.count() > 0):

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
def PostOrDraft(request):
    if request.method == 'POST':
        id = (request.POST.getlist('id[]'))
        print(request.POST['key'])
        deleteditem = Articles.objects.filter(id__in=id)

        try:
            if (deleteditem.count() > 0):

                # row = deleteditem.delete()
                return JsonResponse({
                    'status': True,
                    'ids': list(deleteditem.values_list('id', flat=True).all())
                })

            else:
                raise ValueError('nothing item dont edited')
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


def PostAdd(request):
    form1=AddArticleForm(request.POST or None,request.FILES or None)
    form2=DownloadBoxForm(request.POST or None)
    if request.POST:
        if(form1.is_valid() and form2.is_valid()):
            thought = form1.save(commit=False)
            thought.author =request.user
            thought.save()
            if (form1.cleaned_data.get('mytag').strip() != ''):
                tags: str = form1.cleaned_data.get('mytag')
                Rtags = FindOrCreateTag(tags.strip().split(';'))
                thought.tags.set(Rtags)
            if (form1.cleaned_data.get('categories') != ''):
                thought.categories.set(form1.cleaned_data.get('categories'))
            box=form2.save(commit=False)
            box.Post=thought
            box.save()
            thought.downloadbox=box
            thought.save()
            messages.success(request, "پست با موفقیت ایجاد شد")
            return HttpResponseRedirect(reverse('post_admin'))

    return render(request,'Post/addPost.html',{
        'form':form1,
        'box_download':form2
    })

def EditPost(request,id):
    form1_instance = Articles.objects.filter(id=id).first()
    print(form1_instance)
    form2_instance = DownloadBox.objects.filter(pk=form1_instance.downloadbox.id).first()
    print(form2_instance)
    form1 = AddArticleForm(instance=form1_instance)
    form2 = DownloadBoxForm(instance=form2_instance)
    form1.fields['mytag'].initial=";".join(list(form1_instance.tags.values_list('title', flat=True)))
    if request.method == "POST":
        form1 = AddArticleForm(request.POST, request.FILES, instance=form1_instance)
        form2 = DownloadBoxForm(request.POST, instance=form2_instance)
        if form1.is_valid() and form2.is_valid():
            form2.save()
            thought=form1.save()
            if (form1.cleaned_data.get('mytag').strip() != ''):
                tags: str = form1.cleaned_data.get('mytag')
                Rtags = FindOrCreateTag(tags.strip().split(';'))
                thought.tags.set(Rtags)
            if (form1.cleaned_data.get('categories') != ''):
                thought.categories.set(form1.cleaned_data.get('categories'))
            messages.success(request, 'پست با موفقیت بروزرسانی شد')
            return redirect(reverse('post_admin'))

    context = {
        'form': form1,
        'box_download': form2,
        'old':form1_instance,
        'cat':list(form1_instance.categories.values_list('id', flat=True)),
    }

    return render(request, 'Post/editPost.html', context)