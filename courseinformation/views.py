from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Student,Subject,References
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html',{})

@login_required
def syllabus(request):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    return render(request,'syllabus.html',{'subjects':subjects})

@login_required
def reference(request):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    return render(request,'reference.html',{'subjects':subjects})

@login_required
def syllabusdetail(request,id):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    subject=Subject.objects.filter(subjectid=id)[0]
    return render(request,'syllabusdetail.html',{'subjects':subjects,'subject':subject})

@login_required
def referencedetails(request,id):
    student=Student.objects.filter(username=request.user.username)[0]
    subjects=Subject.objects.filter(department=student.department,year=student.year,semester=student.semester)
    reference=References.objects.filter(subjectid=id)[0]
    return render(request,'referencedetails.html',{'subjects':subjects,'reference':reference})