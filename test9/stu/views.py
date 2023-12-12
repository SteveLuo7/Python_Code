from django.http import HttpResponse
from django.shortcuts import render

from stu.models import insetStu


# Create your views here.
def register(request):
    return render(request,'register.html')


def addStu(request):
    #   get request information
    sname = request.POST.get('sname')
    cname = request.POST.get('cname')
    coursenames = request.POST.getlist('coursename')

    #   insert the data to database

    flag = insetStu(sname,cname,coursenames)

    if flag:
        return HttpResponse('Register Success')
    return HttpResponse('Register Failed')