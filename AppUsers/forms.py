from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppUsers.models import Users
from django import forms


class SignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15) 
   # profilePic=forms.ImageField(required=False)


    

    class Meta:
        model =User
        fields=('username','email','first_name','last_name','password1')
