from django.urls import path
from .views import MainMenu,addMenu,MenuItem,EditMenuItem,edaitStatus,deleteItem
urlpatterns=[

    path('',MainMenu.as_view(),name="MangeMenu"),
    path('<str:menu>',MenuItem.as_view(),name="Menu"),
    path('add/<str:menu>',addMenu.as_view(),name="addMenu"),
    path('edit/<str:menu>-<int:id>',EditMenuItem.as_view(),name="edit_menu_item"),
    path('editstatus/', edaitStatus, name="edit_status_item"),
    path('deleteitem/', deleteItem, name="delete_item"),

]