from django.db import models

# Create your models here.
from AppUsers import models as modelUser
from AppProject import models as project
# Create your models here.
class Donation(models.Model):
    userID=models.ForeignKey(modelUser.Users,on_delete=models.CASCADE)
    donationTime=models.DateTimeField()
    donationAmount=models.FloatField()
    projectID=models.ForeignKey(project.Projects, on_delete=models.CASCADE)