from django.urls import path
from .views import addProductView
urlpatterns=[
    path('add',addProductView,name="add_product")
]