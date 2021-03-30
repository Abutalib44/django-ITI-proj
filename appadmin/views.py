from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from AppCategory.models import category
import AppUsers.models as users_models
from django.urls import reverse
from AppUsers.models import Users,optional_info
from AppProject.models import Projects, projectImg,tagProject
from django.contrib.auth.decorators import login_required

@login_required
def adminpage(request):
    if request.method == "GET":
        categories_ = category.objects.all()
        optional_infos_=optional_info.objects.all()
        projects_=Projects.objects.all()
        return render(request, "ِadminpage.html", {"categories": categories_,"optional_infos": optional_infos_,"projects":projects_,"msg":""})


# Create your views here.
@login_required
def createCat(request):
    if request.method == "POST":
        category.objects.create(categoryName=request.POST["Category"])
    return redirect(reverse("appadmin:home"))

@login_required
def createOptionInfo(request):
    if request.method == "POST":
        optional_info.objects.create(optionName=request.POST["OptionInfo"])
    return redirect(reverse("appadmin:home"))


@login_required
def delete_Cat(request,Cat_ID):
    if request.method == "GET": 
        category.objects.get(id=Cat_ID).delete()
    return redirect(reverse("appadmin:home"))

@login_required
def delete_OptionInfo(request,Opt_ID):
    if request.method == "GET":           
        optional_info.objects.get(id=Opt_ID).delete()
    return redirect(reverse("appadmin:home"))

@login_required
def select_five(request,pid):
    if request.method == "GET":           
        print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        print("1")
        
        if Projects.objects.get(id=pid).isSelect:
            selectItem=Projects.objects.get(id=pid)
            selectItem.isSelect = False
            selectItem.save()
            print("2")
        else:
            if Projects.objects.filter(isSelect=1).count()<5:
                print("3")
                selectItem=Projects.objects.get(id=pid)
                selectItem.isSelect = True
                selectItem.save()
            else:
                print("4")
                categories_ = category.objects.all()
                optional_infos_=optional_info.objects.all()
                projects_=Projects.objects.all()
                return render(request, "ِadminpage.html", {"categories": categories_,"optional_infos": optional_infos_,"projects":projects_,"msg":"only select five projects at most"})

    return redirect(reverse("appadmin:home"))

@login_required
def reportPro(request, pro_id):
    getPro = Projects.objects.filter(id=pro_id).first()
    getPro.isReject = 0
    getPro.save()
    return redirect(reverse("appadmin:home"))


          
    

