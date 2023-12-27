from django.urls import path

from Home.views import HomePage

urlpatterns=[
    path('',HomePage())
]