from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver







# Create your models here.
class Users(models.Model):
    userAdmin=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(null=True,max_length=15, blank=True) 
    isActive=models.BooleanField(default=False)
    isAdmin=models.BooleanField(default=False)
    profilePic=models.ImageField(null=True,upload_to = "images/user/" , blank=True )
    creationTime= models.DateTimeField(null=True)
    token_used_to_active =models.CharField(null=True,max_length=30 , blank=True)

    def __str__(self):
        return str(self.userAdmin)
    


# #@receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Users.objects.create(userAdmin=instance)
    




class optional_info(models.Model):
    optionName= models.CharField(max_length=30)  
    optionImg= models.ImageField(upload_to = "images/")


class user_optional_info(models.Model):
    option_info=models.ForeignKey('optional_info',on_delete=models.CASCADE)
    userID=models.ForeignKey('Users',on_delete=models.CASCADE)
    optionValue= models.CharField(max_length=30)  


    

