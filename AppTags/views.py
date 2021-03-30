from django.shortcuts import render
from django.http import HttpResponse
from .models import Tags
# Create your views here.

def createTag(request):

    # Tags.objects.create(tagName='School')
    # Tags.objects.create(tagName='Clean')
    # Tags.objects.create(tagName='Cliver')
    return HttpResponse('good tag')
