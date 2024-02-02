from django.urls import path
from .views import ContactList,Delete_Contact,SingleContact
urlpatterns=[
    path("",ContactList.as_view(),name="contact_list"),
    path("delete/<pk>",Delete_Contact,name="delete_contact"),
    path("<pk>",SingleContact.as_view(),name="single_contact")
]