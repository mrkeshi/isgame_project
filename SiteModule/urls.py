from django.urls import path
from .views import addSocialLink,SocialLinks,EditSocialItem,delete_item
urlpatterns=[


    path('',SocialLinks.as_view(),name="social_link"),
    path('add/',addSocialLink.as_view(),name="add_social_link"),
    path('edit/<int:id>',EditSocialItem.as_view(),name="edit_social_link"),
    path('deleteitem/<int:id>', delete_item, name="delete_social"),

]