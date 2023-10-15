from django.urls import path,include
from .views import dasboard_class
from Menu import views
urlpatterns=[
    path('',dasboard_class.dashboard_view,name="dashboard"),
    path('Menu/',include('Menu.urls')),
    path('setting/',include('SiteModule.urls')),
    path('',include('Post.urls'))
]