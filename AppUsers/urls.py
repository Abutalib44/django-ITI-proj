from django.contrib import admin
from django.urls import path,include
from .views import signup,active , checkLog

urlpatterns = [
    path('signup',signup,name='signup'),
    path('active/<email>/<token>',active,name='active'),
    path('logout',checkLog,name='checkLog'),
]
