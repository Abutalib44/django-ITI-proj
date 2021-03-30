from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import ProjectForm
from AppCategory.models import category
from .models import projectImg
import AppUsers.models as users_models
from AppTags.models import Tags
from django.urls import reverse
from AppUsers.models import Users
from AppProject.models import Projects, projectImg,tagProject
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def createProject(request):
    
    categories = category.objects.all()
    tags = Tags.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        details = request.POST["details"]
        category_value = int(request.POST["category"])
        total_target = request.POST["totalTarget"]
        start_time = request.POST["startTime"]
        end_time = request.POST["endTime"]
        # user_id = Users.objects.get(id=1)
        x = category.objects.get(id=category_value)

        UserID = Users.objects.get(userAdmin=request.user)
       

        projectID=Projects.objects.create(title=title, details=details, catID=x, 
            startTime=start_time, endTime=end_time, totalTarget=total_target , userID = UserID )

        filepath = request.FILES.getlist('files') if 'files' in request.FILES else False
        for file in filepath:
            print(file)
            projectImg.objects.create(projectID=projectID , imgPath=file)

        tagg = request.POST.getlist('tag') if 'tag' in request.POST else False
        for Stag in tagg:
            print(Stag)
            tagProject.objects.create(projectID=projectID, tagID=Tags.objects.get(id=int(Stag)))

        
        return redirect('../../home/allProject')
    else:
        return render(request, "create_project.html", {
            "categories": categories,
            "tags": tags
            })

@login_required
def create_tags(request):
    if request.method == "POST":
        Tags.objects.create(tagName=request.POST["tag"])

    return redirect(reverse("AppProject:create"))
    

