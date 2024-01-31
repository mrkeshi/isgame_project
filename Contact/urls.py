from django.urls import path
from .views import ContactList,Delete_Contact
urlpatterns=[
    path("",ContactList.as_view(),name="contact_list"),
    path("/delete/<pk>",Delete_Contact,name="delete_contact")
],