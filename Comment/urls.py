from django.urls import path
from . import views
urlpatterns = [
    path('comment', views.CommentManger.as_view(), name="comment_admin"),
    path('comment/delete/', views.CommentDelete, name="comment_delete_admin"),
    path('comment/filter',views.ListComment,name="filter_comment_admin"),
    path('comment/draft', views.CommentOrDraft, name="comment_draft_request"),]