from django.urls import path
from .views import addProductView,ProductManage
urlpatterns=[
    path('add',addProductView,name="add_product"),
    path('',ProductManage.as_view(),name="product_manage")
]