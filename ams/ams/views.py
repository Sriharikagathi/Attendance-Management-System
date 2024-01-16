from django.shortcuts import render,HttpResponse,redirect
from mylogin.models import Student
from mansys.models import *
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
# from django.http import JsonResponse
# def save_to_session(request):
#     if request.method == 'POST':
#         key = request.POST.get('key')
#         value = request.POST.get('value')
#         request.session[key] = value
#         request.session.save()
#         return JsonResponse({'status': 'success'})
#     return JsonResponse({'status': 'error'})
