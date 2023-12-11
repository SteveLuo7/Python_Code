from django.http import HttpResponse
from django.shortcuts import render

from stu.models import Student


# Create your views here.
def index_view(request):
    return render(request,'register.html')


def register(request):
    #   get request code
    sname = request.POST.get('sname','')
    spwd = request.POST.get('spwd','')

    #   save to the database
    student = Student(sname=sname,spwd=spwd)
    student.save()

    return HttpResponse('Register Success')


def show(request):
    #   inquire all the information of students QuerySet[]
    stuList = Student.objects.all()

    return render(request,'show.html',{'stuList':stuList})