from django.db import models
from AppUsers import models as modelUser
from AppCategory import models as modelCat
from AppTags import models as modelTag
# Create your models here.
class Projects(models.Model):

    title=models.CharField(max_length=30)
    details=models.CharField(max_length=250)
    userID=models.ForeignKey(modelUser.Users,on_delete=models.CASCADE, null=True)
    catID=models.ForeignKey(modelCat.category,on_delete=models.CASCADE)
    actualDonation=models.IntegerField(default=0)
    totalTarget=models.IntegerField()
    startTime=models.DateTimeField()
    endTime=models.DateTimeField()
    rate=models.IntegerField(default=0)
    NUN_users_make_rate=models.IntegerField(default=0)
    NUN_users_make_Donate=models.IntegerField(default=0)
    isSelect=models.BooleanField(default=False)
    isReject=models.BooleanField(default=False)

class tagProject(models.Model):
    tagID=models.ForeignKey(modelTag.Tags,on_delete=models.CASCADE)
    projectID=models.ForeignKey(Projects,on_delete=models.CASCADE)

    class Meta:
        unique_together = (('tagID', 'projectID'))


class projectImg(models.Model):
    projectID=models.ForeignKey('Projects',on_delete=models.CASCADE)
    imgPath=models.ImageField(upload_to = "images/project/")
  

class comments(models.Model):
    projectID=models.ForeignKey('Projects',on_delete=models.CASCADE) 
    commentStr=models.TextField()
    replay=models.ForeignKey('comments',on_delete=models.CASCADE , null=True)
    userID=models.ForeignKey(modelUser.Users,on_delete=models.CASCADE)
    startTime=models.DateTimeField()
    isReject=models.BooleanField(default=False)






   



