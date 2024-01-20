from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from mansys.models import *
from django.contrib import messages
from .models import Student
from django.contrib.auth.decorators import login_required

# from django.http import JsonResponse
# from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
def register(request):
    if request.method=='POST':
        user=request.POST['facultyid']
        email=request.POST['email']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        if(password1==password2):
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(username=user).exists():
                messages.info(request,'User Already Exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password is not same')
            return redirect(request,'register')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        user1=request.POST['facultyid']
        password1=request.POST['Password1']
        user=auth.authenticate(username=user1,password=password1)
        if user is not None:
            request.session['username']=user1
            auth.login(request,user)
            return redirect('facultyInfo')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
@login_required(login_url="/log/login/")
def facultyInfo(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        request.session[key] = value
        request.session.save()
    user3=request.session.get('username')
    details=User.objects.filter(username=user3)
    dictt=[]
    all_branches=[]
    sems=[]
    subs=[]
    sectionss=[]
    branches=FACULTY.objects.filter(facultyid=user3).values('branch')
    for i in branches:
        if i['branch'] not in dictt:
                dictt.append(i['branch'])
        all_branches.append(i['branch'])
    semester=FACULTY.objects.filter(facultyid=user3).values('semester')
    for i in semester:
        sems.append(i['semester'])
    subject_code=FACULTY.objects.filter(facultyid=user3).values('subjectid')
    for i in subject_code:
        subs.append(i['subjectid'])
    sections=FACULTY.objects.filter(facultyid=user3).values('section')
    for i in sections:
        sectionss.append(i['section'])
    detailss=[all_branches,sems,subs,sectionss]
    d=[]
    for i in range(len(detailss[0])):
        l = []
        for j in detailss:
          if i < len(j):
                l.append(j[i])
        d.append(l)
    length1=len(detailss)
    print(d)
    return render(request,'facultyInfo.html',{"usr":user3,"branches":dictt,"details":d,"len1":length1})

def studentlist(request):
    pass
