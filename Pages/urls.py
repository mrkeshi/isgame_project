from django.urls import path
from .views import PageList,DeletePage,PageAdd,EditPage
urlpatterns=[
    path('',PageList.as_view(),name="page_list"),
    path('delete/<pk>',DeletePage,name="page_delete"),
    path('add',PageAdd.as_view(),name='add_page'),
    path('edit/<int:pk>',EditPage.as_view(),name="edit_page")
]