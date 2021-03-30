from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.db import IntegrityError, connection, transaction
import datetime
from AppProject.models import comments , Projects , projectImg
from AppUsers.models import Users
from .models import Donation
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    #user_ID = Users.objects.get(userAdmin=request.user).id
   
    cursor = connection.cursor()
 
    Featured = []
    maxRate = []
    lastProject = []
    
    
    FeaturedSelect = "SELECT p.id as idp, p.title as title, p.details , p.totalTarget  , p.rate , p.NUN_users_make_rate , p.actualDonation , c.id as catID , c.categoryName  from AppProject_projects p join AppCategory_category c on c.id = p.catID_id   where p.isSelect= 1 and p.isReject = 0"
    cursor.execute(FeaturedSelect)
    results = cursor.fetchall()
    for c,row in enumerate(results):

        img=projectImg.objects.filter(projectID = Projects.objects.get(id=row[0])).first()
        Featured.append({ 'id' : '{}' .format(row[0]),
               'title': '{}'  .format(row[1]),
               'details' : '{}'  .format(row[2]),
               'totalTarget' : '{}'  .format(row[3]),
               'rate' : '{}'  .format(row[4]),
               'NUN_users_make_rate' : '{}'  .format(row[5]),
               'actualDonation' : '{}'  .format(row[6]),
               'catID' : '{}'  .format(row[7]),
               'categoryName' : '{}'  .format(row[8]),
               'img':img.imgPath
        })


    recommended = "SELECT p.id as idp, p.title as title, p.details , p.totalTarget , p.rate , p.NUN_users_make_rate , p.actualDonation , c.id as catID , c.categoryName  from AppProject_projects p join AppCategory_category c on c.id = p.catID_id  where  p.isReject = 0  ORDER by p.rate limit 5 "
    cursor.execute(recommended)
    results = cursor.fetchall()
    for c,row in enumerate(results):
        
        img=projectImg.objects.filter(projectID = Projects.objects.get(id=row[0])).first()
       
        maxRate.append({ 'id' : '{}' .format(row[0]),
               'title': '{}'  .format(row[1]),
               'details' : '{}'  .format(row[2]),
               'totalTarget' : '{}'  .format(row[3]),
               'rate' : '{}'  .format(row[4]),
               'NUN_users_make_rate' : '{}'  .format(row[5]),
               'actualDonation' : '{}'  .format(row[6]),
               'catID' : '{}'  .format(row[7]),
               'categoryName' : '{}'  .format(row[8]),
               'img':img.imgPath
        })    

    last = "SELECT p.id as idp, p.title as title, p.details , p.totalTarget , p.rate , p.NUN_users_make_rate , p.actualDonation , c.id as catID , c.categoryName  from AppProject_projects p join AppCategory_category c on c.id = p.catID_id  where  p.isReject = 0  limit 5 "
    cursor.execute(last)
    results = cursor.fetchall()
    for c,row in enumerate(results):

        img=projectImg.objects.filter(projectID = Projects.objects.get(id=row[0])).first()

        lastProject.append({ 'id' : '{}' .format(row[0]),
               'title': '{}'  .format(row[1]),
               'details' : '{}'  .format(row[2]),
               'totalTarget' : '{}'  .format(row[3]),
               'rate' : '{}'  .format(row[4]),
               'NUN_users_make_rate' : '{}'  .format(row[5]),
               'actualDonation' : '{}'  .format(row[6]),
               'catID' : '{}'  .format(row[7]),
               'categoryName' : '{}'  .format(row[8]),
               'img':img.imgPath
        })    
              
    return render(request,"Home.html", {'Featured':Featured , 'maxRate':maxRate , 'lastProject':lastProject , 'all':'all'} )



def project(request,pro_id , msg=None ) :

    cursor = connection.cursor()
    projectDetails = {}
    projectComment=[]
    
    FeaturedSelect = "SELECT p.id as idp, p.title as title, p.details , p.totalTarget , p.rate , p.NUN_users_make_rate , p.actualDonation , c.id as catID , c.categoryName  from AppProject_projects p join AppCategory_category c on c.id = p.catID_id   where p.id=={} and p.isReject = 0 ".format(pro_id)
    cursor.execute(FeaturedSelect)
    results = cursor.fetchall()
    for c,row in enumerate(results):

       
        tagsProject=[]
        AllProjectTagSelect = "select * from AppTags_tags T join AppProject_tagproject TP on TP.tagID_id = T.id join AppProject_projects P on P.id = TP.projectID_id where P.id= {} and p.isReject = 0".format(row[0]) 
        cursor.execute(AllProjectTagSelect)
        results = cursor.fetchall()
        for c,rowTag in enumerate(results):
            tagsProject.append({ 'id' : '{}' .format(rowTag[0]),
                'tagName': '{}'  .format(rowTag[1])
                })
            # similarPro  
            similarPeoject=[]
            similarPro = "SELECT p.id as idp, p.title as title, p.details , p.totalTarget  , p.rate , p.NUN_users_make_rate , p.actualDonation , c.id as catID , c.categoryName  from AppProject_projects p join AppCategory_category c on c.id = p.catID_id join AppProject_tagproject PT on PT.projectID_id = p.id  where  p.isReject=0 and p.isSelect= 0 and PT.tagID_id = {}".format(rowTag[0])
            cursor.execute(similarPro)
            resultssimilarPro = cursor.fetchall()
            for cS,rowS in enumerate(resultssimilarPro):
                img=projectImg.objects.filter(projectID = Projects.objects.get(id=rowS[0])).first()
                similarPeoject.append({ 'id' : '{}' .format(rowS[0]),
                    'title': '{}'  .format(rowS[1]),
                    'details' : '{}'  .format(rowS[2]),
                    'totalTarget' : '{}'  .format(rowS[3]),
                    'rate' : '{}'  .format(rowS[4]),
                    'NUN_users_make_rate' : '{}'  .format(rowS[5]),
                    'actualDonation' : '{}'  .format(rowS[6]),
                    'catID' : '{}'  .format(rowS[7]),
                    'categoryName' : '{}'  .format(rowS[8]),
                    'img':img.imgPath
                }) 
              



        img=[]
        ImageSelect = "select imgPath from AppProject_projectimg WHERE projectID_id = {} ".format(row[0])
        cursor.execute(ImageSelect)
        resultsImg = cursor.fetchall()
        for i,rowImg in enumerate(resultsImg):
            


            img.append({'imgPath':'{}'.format(rowImg[0])})
            
        
        projectDetails=({ 'id' : '{}'.format(row[0]),
               'title': '{}'  .format(row[1]),
               'details' : '{}'  .format(row[2]),
               'totalTarget' : '{}'  .format(row[3]),
               'rate' : '{}'  .format(row[4]),
               'NUN_users_make_rate' : '{}'  .format(row[5]),
               'actualDonation' : '{}'  .format(row[6]),
               'catID' : '{}'  .format(row[7]),
               'categoryName' : '{}'  .format(row[8])
               })

    CommentSelect = "select C.id as 'idComment',C.startTime ,AU.first_name ,AU.last_name , C.commentStr from AppProject_comments C  join AppUsers_users U on C.userID_id = U.id  join auth_user AU on AU.id = U.userAdmin_id  join AppProject_projects P on P.id = C.projectID_id  and p.isReject = 0  where P.id={} and p.isReject = 0".format(pro_id)

    cursor.execute(CommentSelect)
    results = cursor.fetchall()
    for c,row in enumerate(results):
        projectComment.append({ 'idComment' : '{}' .format(row[0]),
               'timeComment' : '{}'  .format(row[1]),
               'firstName' : '{}'  .format(row[2]),
                'lastName' : '{}'  .format(row[3]),
                'commentStr' : '{}'  .format(row[4]),
        })

   


    if(msg == None):
    
        return render(request,"detailProject.html" ,{'projectDetails':projectDetails, 'tagsProject':tagsProject ,'projectComment':projectComment , 'similarPeoject':similarPeoject , 'img':img , 'msg':'none' } )  

    else:
        return render(request,"detailProject.html" ,{'projectDetails':projectDetails , 'tagsProject':tagsProject ,'similarPeoject':similarPeoject ,'projectComment':projectComment , 'img':img , 'msg':msg } )      
    


@login_required
def addDonate(request ,pro_id):
     if(request.method=='POST'):
         amount = request.POST['amount']
         UserID = request.session.get('USER_ID')
         DateDonate = datetime.datetime.now() 
         Donation.objects.create(projectID=Projects(id=pro_id) , donationAmount=amount , userID=Users(id=UserID) , donationTime = DateDonate)
         getPro = Projects.objects.filter(id=pro_id).first()
         getPro.actualDonation = getPro.actualDonation + int(amount)
         getPro.NUN_users_make_Donate = getPro.NUN_users_make_Donate + 1
         try:
            getPro.save()# Could throw exception
            redirURl='../../{}/{}'.format(pro_id ,'successDonate')
         except IntegrityError:
            transaction.rollback()
         return redirect(redirURl)

@login_required
def addRate(request ,pro_id, msgR):
    getPro = Projects.objects.filter(id=pro_id).first()
    if(msgR == 'yes'):
        getPro.rate = getPro.rate + 1
        getPro.NUN_users_make_rate = getPro.NUN_users_make_rate + 1
    else:
        if(getPro.rate > 0 ):
            getPro.rate = getPro.rate - 1
    
    getPro.save()
    redirURl='../../../{}/{}/'.format(pro_id ,'rating')
    return redirect(redirURl)
            


def allProjects(request):
    
    allProject = []
    
    allTag=[]
    cursor = connection.cursor()
    AllTagSelect = "select * from AppTags_tags " 
    cursor.execute(AllTagSelect)
    results = cursor.fetchall()
    for c,row in enumerate(results):
        allTag.append({ 'id' : '{}' .format(row[0]),
            'tagName': '{}'  .format(row[1])
        })    
    
    if( request.GET.get('searching')):
        searchName=request.GET.get('searching')
    else:
        searchName = None    

    if(searchName == None):
       
        AllProjectSelect = "SELECT p.id as idp, p.title as title, p.details , p.totalTarget , p.rate , p.NUN_users_make_rate , p.actualDonation , c.id as catID , c.categoryName  from AppProject_projects p join AppCategory_category c on c.id = p.catID_id where  p.isReject = 0 "
        cursor.execute(AllProjectSelect)
        results = cursor.fetchall()
        for c,row in enumerate(results):
            
            
            img=projectImg.objects.filter(projectID = Projects.objects.get(id=row[0])).first()
            
            tagsProject=[]
            AllProjectTagSelect = "select * from AppTags_tags T join AppProject_tagproject TP on TP.tagID_id = T.id join AppProject_projects P on P.id = TP.projectID_id where P.id= {} and p.isReject = 0".format(row[0]) 
            cursor.execute(AllProjectTagSelect) 
            results = cursor.fetchall()
            for c,rowTag in enumerate(results):
                    tagsProject.append({ 'id' : '{}' .format(rowTag[0]),
                        'tagName': '{}'  .format(rowTag[1])
                    })

            allProject.append({ 'id' : '{}' .format(row[0]),
                    'title': '{}'  .format(row[1]),
                    'details' : '{}'  .format(row[2]),
                    'totalTarget' : '{}'  .format(row[3]),
                    'rate' : '{}'  .format(row[4]),
                    'NUN_users_make_rate' : '{}'  .format(row[5]),
                    'actualDonation' : '{}'  .format(row[6]),
                    'catID' : '{}'  .format(row[7]),
                    'categoryName' : '{}'  .format(row[8]),
                    'tags' : tagsProject ,
                    'img': img.imgPath

                })
            

        return render(request,"allProjects.html"  ,{'allProject':allProject  ,'allTag':allTag }) 

    else:
        AllProjectSelect = "SELECT p.id as idp, p.title as title, p.details , p.totalTarget , p.rate , p.NUN_users_make_rate , p.actualDonation , c.id as catID , c.categoryName  ,T.tagName from AppProject_projects p join AppCategory_category c on c.id = p.catID_id   join AppProject_tagproject PT on PT.projectID_id= p.id join AppTags_tags T on T.id = PT.tagID_id where p.title like '{}' or T.tagName like '{}' and p.isReject = 0 ".format(searchName ,searchName)
        cursor.execute(AllProjectSelect)
        results = cursor.fetchall()
        for c,row in enumerate(results):

            img=projectImg.objects.filter(projectID = Projects.objects.get(id=row[0])).first()

            tagsProject=[]
            AllProjectTagSelect = "select * from AppTags_tags T join AppProject_tagproject TP on TP.tagID_id = T.id join AppProject_projects P on P.id = TP.projectID_id where P.id= {} and p.isReject = 0".format(row[0]) 
            cursor.execute(AllProjectTagSelect)
            results = cursor.fetchall()
            for c,rowTag in enumerate(results):
                    tagsProject.append({ 'id' : '{}' .format(rowTag[0]),
                        'tagName': '{}'  .format(rowTag[1])
                    })

            allProject.append({ 'id' : '{}' .format(row[0]),
                    'title': '{}'  .format(row[1]),
                    'details' : '{}'  .format(row[2]),
                    'totalTarget' : '{}'  .format(row[3]),
                    'rate' : '{}'  .format(row[4]),
                    'NUN_users_make_rate' : '{}'  .format(row[5]),
                    'actualDonation' : '{}'  .format(row[6]),
                    'catID' : '{}'  .format(row[7]),
                    'categoryName' : '{}'  .format(row[8]),
                    'tags' : tagsProject ,
                    'img' : img.imgPath
                })   

            return render(request,"allProjects.html"  ,{'allProject':allProject  ,'allTag':allTag })         
        
 
@login_required
def addComment(request,pro_id):
    redirURl='../../{}'.format(pro_id)
    if(request.method == 'POST'):
        msg = request.POST['msg']
        UserID = Users.objects.get(userAdmin=request.user).id
        DateMsg = datetime.datetime.now() 
        comments.objects.create(projectID=Projects(id=pro_id) , commentStr=msg , userID=Users(id=UserID) , startTime = DateMsg)
        
    return redirect(redirURl)



@login_required
def reportPro(request, pro_id):
    getPro = Projects.objects.filter(id=pro_id).first()
    getPro.isReject = 1
    getPro.save()
    return redirect('/home/allProject')

@login_required
def reportCom(request, c_id):
    getCom = comments.objects.filter(id=c_id ).first()
    pro_id= getCom.projectID.id
    getCom.delete()
    redirURl = '../../{}'.format(pro_id)
    return redirect(redirURl)    








