from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.COOKIES.get('user'):
        user = request.COOKIES.get('user')
        us = user.split(',')
        uname = us[0]
        pwd = us[1]

        return render(request,'login.html',{'uname':uname,'pwd':pwd})
    return render(request,'login.html')


def tologin(request):
    #   get request path
    uname = request.POST.get('uname','')
    pwd = request.POST.get('pwd','')
    flag = request.POST.get('flag','')

    resp = HttpResponse()
    if uname == 'zhangsan' and pwd == '123':
        resp.content = 'Login Success...'
        if flag == '1':
            resp.set_cookie('user',uname+','+pwd,max_age=3*24*60*60,path='/student/login/')
            return resp
        else:
            resp.delete_cookie('user',path='/student/login/')
    else:
        resp.delete_cookie('user',path='/student/login/')
        resp.status_code=302
        resp.setdefault('Location',path='/student/login/')
    return resp