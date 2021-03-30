from django.db import models

# Create your models here.
class Tags(models.Model):
    tagName=models.CharField(max_length=30 , unique=True)
    