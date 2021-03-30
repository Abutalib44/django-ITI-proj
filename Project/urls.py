"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from AppHome.views import home
from django.conf.urls.static import static
from django.conf import settings
#from AppCategory import urls 
#from AppHome import urls 
#from AppProject import urls 
#from AppTags import urls 
#from AppUsers import urls 

urlpatterns = [
    path('user/', include('django.contrib.auth.urls')),
    path('users/', include('AppUsers.urls')),
    path('admin/', admin.site.urls),
    path('tag/', include('AppTags.urls') ),
    path('project/', include('AppProject.urls')),
    path('home/',include('AppHome.urls')),
    path('category/', include('AppCategory.urls')),
    path('AppProfile/', include('AppProfile.urls')),
    path('accounts/profile/',home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('appadmin/', include('appadmin.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)