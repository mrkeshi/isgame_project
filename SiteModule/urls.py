from django.urls import path
from .views import addSocialLink,SocialLinks,EditSocialItem,delete_item,Manage_Settings,WidgetIndex,adsBanner
urlpatterns=[
    path('add/',addSocialLink.as_view(),name="add_social_link"),
    path('edit/<int:id>',EditSocialItem.as_view(),name="edit_social_link"),
    path('deleteitem/<int:id>', delete_item, name="delete_social"),
    path('widget/', WidgetIndex.as_view(), name="setting_widget"),
    path('widget/adsbanner', adsBanner, name="ads_banner"),

    path('',Manage_Settings,name="manage_settings"),


]