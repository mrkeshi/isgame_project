"""isgame_project URL Configuration

The `urlpatterns` list routes URLs to items. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function items
    1. Add an import:  from my_app import items
    2. Add a URL to urlpatterns:  path('', items.home, name='home')
Class-based items
    1. Add an import:  from other_app.items import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from Contact.views import ContactView
from User import views as UserView
from Home import views as HomeView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('contact', ContactView.as_view(), name="contact"),

    path('admin/', admin.site.urls),
                  re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # The CKEditor path
                  path('myadmin/',include('User.urls')),
    path('dashbaord/',include('admin_panel.urls')),
    path('user/resetpassword',UserView.ResetPassword.as_view(),name="resetpassword"),
    path("unicorn/", include("django_unicorn.urls")),
    path('user/resetpassword/<token>', UserView.ResetPasswordConfirm.as_view(), name="resetpassword_confirm"),
    path('',include('UserProfile.urls')),
    path('',include("Home.urls")),



]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

