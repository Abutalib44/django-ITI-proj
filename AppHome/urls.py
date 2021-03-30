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

from django.urls import path,include,re_path
from .views import home,project,allProjects ,addComment , addDonate ,addRate , reportPro , reportCom
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', home),  
    re_path(r'^project/(?P<pro_id>\d+)/$', project),
    re_path(r'^project/addDonate/(?P<pro_id>\d+)/$', addDonate),
    re_path(r'^project/(?P<pro_id>\d+)/(?P<msg>\w+)/$', project),  
    re_path(r'^project/addRate/(?P<pro_id>\d+)/(?P<msgR>\w+)/$', addRate),  
    path('allProject', allProjects), 
    re_path(r'^allProject/$', allProjects),   
    re_path(r'^project/addComment/(?P<pro_id>\d+)/$', addComment), 
    re_path(r'^project/reportPro/(?P<pro_id>\d+)/$', reportPro),   
    re_path(r'^project/reportCom/(?P<c_id>\d+)/$', reportCom),   
]


