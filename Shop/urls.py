from django.urls import path
from .views import addProductView,ProductManage,DeleteProduct,EditProduct
urlpatterns=[
    path('add',addProductView,name="add_product"),
    path('',ProductManage.as_view(),name="product_manage"),
    path('delete/<pk>',DeleteProduct,name="delete_product"),
    path('edit/<pk>',EditProduct,name="edit_product"),
]