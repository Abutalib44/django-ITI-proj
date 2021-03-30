from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users
from django.contrib.auth.hashers import make_password
from AppUsers import views
from .forms import SignupForm
from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from datetime import datetime,timezone
import re
import logging
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth import logout
SERVICE ='smtp.gmail.com:587'
USERNAME= 'djangoproject95@gmail.com'
PASSWORD='hassan@1995'
def send_email(fromaddr, toaddrs, msg,username):

    # Create the plain-text and HTML version of your message
    message = """Subject: Your Active link

    Hi {name}, your link is {link}"""
    try:
    
      #connection = init_connection(SERVICE, USERNAME, PASSWORD)
     
      server = smtplib.SMTP(SERVICE)
      server.ehlo()
      server.starttls()
      server.login(USERNAME,PASSWORD)
      server.ehlo()
      server.sendmail(fromaddr, toaddrs, message.format(name=username,link=msg)) 
      server.quit()
    except:
        logging.critical("cant start connection")

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email =request.POST['email']
            email_check=User.objects.filter(email = email).count()
            phone_=request.POST['phone_number']
            phone_check = re.search("^(01)[0-9]{9}$", phone_)
            if phone_check == None:    
                return render(request,'registration/signup.html',{'form':form,'error_message':" phone number not valid" })
            if email_check > 0 :
                return render(request,'registration/signup.html',{'form':form,'error_message':"This Email already Exist" })
            form.save(commit=True)
            user_name= request.POST['username']
            user_=User.objects.filter(username = user_name ).first()
            user_.is_active=False
            user_.save()
            token = get_random_string(length=32)
            filepath = request.FILES.getlist('pic') if 'pic' in request.FILES else False
            if filepath:
                userimg=filepath[0]
                Users.objects.create(userAdmin=user_,phone_number=phone_,profilePic=userimg,isActive=False,isAdmin=False,creationTime=datetime.now(),token_used_to_active=token)
            else:
                Users.objects.create(userAdmin=user_,phone_number=phone_,isActive=False,isAdmin=False,creationTime=datetime.now(),token_used_to_active=token)     
            link="http://127.0.0.1:8000/users/active/"+user_.email+"/"+token
            send_email("ehabewies5@gmail.com",user_.email,link,user_.username)
            # password = form.cleaned_data.get('password1')
            # userLogin = authenticate(username=user_name, password=password)
            # if userLogin:
            #     login(request, user_)
                
            return redirect('/user/login')
    else:
        form = SignupForm()
        return render(request,'registration/signup.html',{'form':form,'error_message':'' })    
       

def active(request,email,token):
    user=User.objects.filter(email=email).first()
    if user:
        myuser=Users.objects.filter(userAdmin=user).first()
        if myuser:
            datecreate =datetime(myuser.creationTime.year,myuser.creationTime.month,myuser.creationTime.day,myuser.creationTime.hour,myuser.creationTime.minute,myuser.creationTime.second)
            hour=(datetime.now()- datecreate).total_seconds()/(60*60)
            if token == myuser.token_used_to_active and hour < 24 :
                myuser.isActive=True
                myuser.save()
                user.is_active=True
                user.save()
                return redirect("/user/login")
    return redirect("/users/signup" )

def checkLog(request):
    print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    print( request.user.is_authenticated)
    if request.user.is_authenticated:
        logout(request)
        return redirect('../../home')
    else:
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        return redirect("../user/login")   

    
    

