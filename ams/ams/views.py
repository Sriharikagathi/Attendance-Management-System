from django.shortcuts import render,HttpResponse,redirect
from mylogin.models import Student
from mansys.models import *
from django.contrib.auth.decorators import login_required
@login_required(login_url='/log/login/')
def index(request,semester,branch,section,subject):
    if request.method=="POST":
        details=Student.objects.filter(branch=branch,section=section,semester=semester)
        dictt={}
        students_rollnos=[]
        for i in details:
            students_rollnos.append(i.studentid)
        for i in students_rollnos:
            dictt[i]=request.POST.get(f'attendance_{i}')
        b=request.session.get('branch')  
        d=request.POST.get('date')
        ts=request.POST.get('timeslot')
        fid=request.session.get('username')
        sem=request.session.get('semester')
        sec=request.session.get('section')
        suid=request.session.get('subject')
        for i in dictt:
            if dictt[i]=="present":
                dictt[i]=True
            else:
                dictt[i]=False
        for i in dictt:
            if b=="CSE":
                k=CSE(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
            elif b=="ECE":
                k=ECE(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
            elif b=="EEE":
                k=EEE(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
            elif b=="MECH":
                k=MECH(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
            elif b=="CIVIL":
                k=CIVIL(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
            elif b=="CSBS":
                k=CSBS(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
            elif b=="CSM":
                k=CSM(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
            else:
                k=CSD(date=d,semester=sem,section=sec,facultyid=fid,Timeslot=ts,studentid=i,status=dictt[i],subjectid=suid)
                k.save()
    request.session['semester']=semester
    request.session['branch']=branch
    request.session['section']=section
    request.session['subject']=subject
    details=Student.objects.filter(branch=branch,section=section,semester=semester)
    dictt={}
    students_rollnos=[]
    for i in details:
        students_rollnos.append(i.studentid)
    return render(request,'studentlist.html',{'details':details})
def attendance(request):
    br=request.session.get('branch')
    sem=request.session.get('semester')
    li=[]
    if br=="CSE":
        obj=CSE.objects.filter(semester=sem)       
    elif br=="ECE":
        obj=ECE.objects.filter(semester=sem)
    elif br=="EEE":
        obj=EEE.objects.filter(semester=sem)
    elif br=="MECH":
        obj=MECH.objects.filter(semester=sem)
    elif br=="CIVIL":
        obj=CIVIL.objects.filter(semester=sem)
    elif br=="CSBS":
        obj=CSBS.objects.filter(semester=sem)
    elif br=="CSM":
        obj=CSM.objects.filter(semester=sem)
    else:
        obj=CSD.objects.filter(semester=sem)
    for i in obj:
        li.append(i.subjectid)
    li=list(set(li))
    print(li)