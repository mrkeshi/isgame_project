from django.urls import path
from .views import PageList
urlpatterns=[
    path('',PageList.as_view(),name="page_list")
]