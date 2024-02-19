from django.urls import path

from Home.views import HomePage,CategoryPage

urlpatterns=[
    path('',HomePage,name="HomePage"),
    path('category/<str:slug>',CategoryPage.as_view(),name="category_page")
]