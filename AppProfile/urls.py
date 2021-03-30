from django.urls import path,include
from .views import Profile,edit_optionalinfo,delete_pro, deleteUser
urlpatterns = [
     path('', Profile),
     path('edit_optionalinfo/', edit_optionalinfo),
     path('delete_pro/<int:pro_ID>', delete_pro),
     path('deleteUser/', deleteUser),
     
]
