from copy import copy
from datetime import datetime, timedelta

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView

from utils import Http_service
from .forms import ReplayCommentForm
from .models import Comment
from django.contrib import messages

# Create your views here.
class CommentManger(TemplateView):
    template_name = 'Comment/ListComment.html'

    def get_context_data(self, **kwargs):
        myComment: Comment = None
        con = super().get_context_data(**kwargs)

        con['times'] = Comment.objects.all().annotate(date=TruncMonth('created')).values('date').annotate(
            count=Count('id')).order_by('-date')
        print(con['times'])
        return con


class ReplayComment(FormView):
    template_name = "Comment/ReplayComment.html"
    form_class = ReplayCommentForm
    success_url = reverse_lazy('comment_admin')
    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['c'] = Comment.objects.filter(id=self.kwargs['id']).first()
        return content
    def form_valid(self, form):

        user = self.request.user

        comment = Comment(name=user.get_full_name(), email=user.email, message=form.cleaned_data.get('message'),
                          ip=Http_service.get_client_ip(self.request), come_id=self.kwargs['id'],post_id=self.get_context_data()['c'].post.id,active=True)
        comment.save()
        s:Comment=Comment.objects.filter(id=self.get_context_data()['c'].id).first()
        s.active=True
        s.save()


        messages.success(self.request,"نظر با موفقیت پاسخ داده شد.")
        return super().form_valid(form)
def ListComment(request):
    myComment: Comment = None
    page: int = 1
    if (request.GET.get('page')):
        page: int = request.GET.get('page')
    myComment = Comment.objects
    if (request.GET.get('title')):
        myComment = myComment.filter(
            Q(message__icontains=request.GET.get('title')) | Q(name__icontains=request.GET.get('title')))

    if (request.GET.get('date')):
        if (request.GET.get('date') != 'all'):
            ti = request.GET.get('date')
            start = datetime.strptime(ti, '%Y%m%d')
            next_month_start = (start.replace(day=28) + timedelta(days=4))
            myComment = myComment.filter(created_date__range=(start, next_month_start))

    paginator = Paginator(myComment.all().order_by('-id'), 10)
    myArticles = paginator.page(page)

    return render(request, 'Comment/includes/ListCommentsComponents.html', {
        'Comments': myArticles,
        'paginator': paginator
    })


def CommentDelete(request):
    if request.method == 'POST':
        id = (request.POST.getlist('id[]'))

        deleteditem = Comment.objects.filter(id__in=id)

        try:
            if (deleteditem.count() > 0):   
                ali = list(deleteditem.values_list('id', flat=True))
                deleteditem.delete()
                return JsonResponse({
                    'status': True,
                    'ids': ali
                })

            else:
                raise ValueError('nothing item dont delted')
        except:
            return JsonResponse({
                'status': False})


def CommentOrDraft(request):
    if request.method == 'POST':
        id = (request.POST.getlist('id[]'))

        deleteditem = Comment.objects.filter(id__in=id)

        try:
            if (deleteditem.count() > 0):
                if (request.POST['key'] == "draft"):

                    deleteditem.update(active=False)

                else:
                    deleteditem.update(active=True)

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
