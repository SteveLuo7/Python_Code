from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    return render(request,'helloworld.html' )

def login_view(request):
    return render(request,'login.html')

def tologin_view(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')
    if uname == 'zhangsan' and pwd == '123':
        return HttpResponse('Login Success')
    return HttpResponse('Login Failed')

