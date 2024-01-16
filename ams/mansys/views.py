from django.shortcuts import render
from django.http import HttpResponse
from .models import CSE,ECE,EEE,CIVIL,MECH,CSM,CSBS,CSD,FACULTY,STUDENTDETAILS

def BRANCH(request,branch):
     if(branch=="CSE"):
          cse=CSE.objects.all()
          return render(request,'')
     elif(branch=="ECE"):
          ece=ECE.objects.all()
     elif(branch=="EEE"):
          eee=EEE.objects.all()
     elif(branch=="MECH"):
          mech=MECH.objects.all()
     elif(branch=="CIVIL"):
          civil=CIVIL.objects.all()
     elif(branch=="CSM"):
          csm=CSM.objects.all()
     elif(branch=="CSD"):
          csd=CSD.objects.all()
     elif(branch=="CSBS"):
          csbs=CSBS.objects.all()
     return render(request,)
def faculty(request):
     faculty=FACULTY.objects.all()
def student_details(request):
     studentdetails=STUDENTDETAILS.objects.all()
def index(request):
     return render(request,'index.html')

# Create your views here.
def create(request):
    pass
def update(request):
     pass
def delete(request):
     pass
def read(request):
     pass

