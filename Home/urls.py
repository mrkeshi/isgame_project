from django.urls import path
from Home.views import SinglePost
from Home.views import HomePage,CategoryPage,Category,TagPage

urlpatterns=[
    path('',HomePage,name="HomePage"),
    path('<str:slug>',SinglePost.as_view(),name="single_post"),
    path('category/<str:title>',Category,name="category_page"),
    path('tag/<str:title>',TagPage.as_view(),name="tag_page"),
]