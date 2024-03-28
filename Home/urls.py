from django.urls import path
from Home.views import SinglePost
from Home.views import HomePage,CategoryPage,Category,TagPage
from Home.Page import CategoryPage,Blog
urlpatterns=[
    path('',HomePage,name="HomePage"),
    path('<str:slug>',SinglePost.as_view(),name="single_post"),
    path('category/<str:title>',CategoryPage,name="category_page"),
    path('tag/<str:title>',TagPage.as_view(),name="tag_page"),
    path('blog',Blog,name="blog")
]