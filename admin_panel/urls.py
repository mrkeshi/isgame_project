from django.urls import path,include
from .views import dasboard_class
from SiteModule import views as SiteModule
from Menu import views

urlpatterns=[
    path('',dasboard_class.dashboard_view,name="dashboard"),
    path('Menu/',include('Menu.urls')),
    path('setting/',include('SiteModule.urls')),
    path('',include('Post.urls')),
    path('contacts/',include('Contact.urls')),
    path('gallery/',SiteModule.GalleryMange.as_view(),name="media_list"),
    path('delete/delete',SiteModule.DeletedItems,name="delete_gallery"),
    path('gallery/add',SiteModule.Add,name="gallery_add"),
    path('Pages/',include('Pages.urls')),
    path('shop/',include('Shop.urls'))

]