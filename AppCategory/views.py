from django.shortcuts import render
from django.http import HttpResponse
from .models import category
# Create your views here.

def createCat(request):
    category.objects.create(categoryName='Medical')
    category.objects.create(categoryName='Memorial')
    category.objects.create(categoryName='Emergency')
    category.objects.create(categoryName='Nonprofit')
    category.objects.create(categoryName='Animal')
    category.objects.create(categoryName='Education')

    return HttpResponse("good cat")



          