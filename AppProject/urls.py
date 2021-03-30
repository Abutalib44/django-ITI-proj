
from django.urls import path,include
from .views import createProject, create_tags

app_name="AppProject"

urlpatterns = [
    path('create/', createProject, name='create'),
    path("create_tag/", create_tags, name='create_tag')
]
