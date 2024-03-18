from django.urls import path
from Home.views import SinglePost
from Home.views import HomePage,CategoryPage

urlpatterns=[
    path('',HomePage,name="HomePage"),
    path('<str:slug>',SinglePost.as_view(),name="single_post"),
    path('category/<str:slug>',CategoryPage.as_view(),name="category_page")
]