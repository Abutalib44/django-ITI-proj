from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.views.generic import ListView
from AppUsers.models import optional_info,user_optional_info
from AppUsers.models import Users
from AppProject.models import Projects
from AppHome.models import Donation
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Profile(request):
     UserID = Users.objects.get(userAdmin=request.user)
     if request.method == "GET":
         optionalinfo=optional_info.objects.all()
         for opt in optionalinfo:
              user_opt_count=user_optional_info.objects.filter(option_info=opt,userID=UserID).count()
              if user_opt_count==0:
                   user_optional_info.objects.create(option_info=opt,userID=UserID)  
         user_opt=user_optional_info.objects.filter(userID=UserID)     
         userproject=Projects.objects.filter(userID=UserID)
         Donationuser=Donation.objects.filter(userID=UserID)
         return render(request, 'profile.html', {'users':UserID,'user':request.user,'user_opt':user_opt,'userproject':userproject,'Donationuser':Donationuser})
     if request.method == "POST":
          user_=User.objects.filter(username= request.user.username).first()
          user_.first_name=request.POST['fname']
          user_.last_name=request.POST['lname']
          user_.save()
          UserID.phone_number=request.POST['phone_number']
          filepath = request.FILES['profilePic'] if 'profilePic' in request.FILES else False
          if filepath:
               UserID.profilePic = request.FILES["profilePic"]          
          UserID.save()
          return redirect('/AppProfile/')
         
@login_required
def edit_optionalinfo(request):
     if request.method == "POST": 
          UserID = Users.objects.get(userAdmin=request.user)
          optionalinfo=optional_info.objects.all()
          for opt in optionalinfo:
               opt_name=opt.optionName
               value=request.POST[opt_name]
               user_optional_info.objects.filter(option_info=opt,userID=UserID).update(optionValue=value)
     return redirect('/AppProfile/')

@login_required
def delete_pro(request,pro_ID):
     if request.method == "GET": 
          if Projects.objects.get(id=pro_ID).totalTarget < 250000 :
               Projects.objects.get(id=pro_ID).delete()

          

     return redirect('/AppProfile/')

@login_required
def deleteUser(request):
     if(request.method=="POST"):
          userPass= request.POST['password']
          countRow=User.objects.filter(username= request.user.username , password=userPass )
          if(countRow.count() == 0):
               msg="enter correct data"
               return render(request,"deleteUser.html" , {'msg':msg} )   
          else:    
               countRow.first().delete() 
               logout(request)
               return redirect ('../../user/login/')
     else:
          return render(request,"deleteUser.html" ,{'msg':''})     



