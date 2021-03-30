from django.db import models

# Create your models here.

class category(models.Model):
    categoryName=models.CharField(max_length=30 , unique=True)
