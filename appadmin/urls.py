
from django.urls import path,include
from .views import adminpage,createCat,createOptionInfo,delete_Cat,delete_OptionInfo,select_five,reportPro
app_name="appadmin"
urlpatterns = [
    path('', adminpage ,name="home"),
    path('createCat/', createCat ,name="createCat"),
    path('createOptionInfo/', createOptionInfo ,name="createOptionInfo"),
    path('delete_Cat/<int:Cat_ID>', delete_Cat ,name="delete_Cat"),
    path('delete_OptionInfo/<int:Opt_ID>', delete_OptionInfo ,name="delete_OptionInfo"),
    path('select_five/<int:pid>', select_five ,name="select_five"),
    path('reportPro/<int:pro_id>', reportPro ,name="reportPro"),
   
]
