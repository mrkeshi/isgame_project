from  django.urls import path
from . import views
urlpatterns=[
    path('register',views.auth_admin_register.as_view(),name='admin_register'),
    path('login',views.auth_admin_login.as_view(),name='admin_login'),
    path('logout',views.mylogout,name="admin_logout"),
    path('user_sission',views.User_sissions.as_view(), name = "user_sission"),
    path('user_sission/<pk>', views.Delete_session, name="delete_session"),
    path('profile', views.Profile, name="profile_admin"),
]