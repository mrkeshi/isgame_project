from django.urls import path
from .views import RegisterUser,LoginUser,UserProfile
urlpatterns=[
    path("login",LoginUser.as_view(),name='user_profile_login'),
    path("register",RegisterUser.as_view(),name="user_profile_register"),
    path("profile",UserProfile.as_view(),name="UserProfile")
]