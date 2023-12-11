from django.http import HttpResponse
from django.shortcuts import render

from stu.models import Student


# Create your views here.
def login_view(request):

    return render(request,'login.html')


def tologin(request):
    sname = request.POST.get('sname','')
    spwd = request.POST.get('spwd','')

    #   yanzheng
    count = Student.objects.filter(sname=sname,spwd=spwd).count()
    if count == 1 :
        return HttpResponse('Login Success')
    return  HttpResponse('Login Fail')