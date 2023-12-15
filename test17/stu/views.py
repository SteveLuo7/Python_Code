from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def setCookieInfo(request):
    response = HttpResponse()
    # response.set_cookie('uname','zhangsan',max_age=1*24*60*60,path='/abc/')
    response.set_signed_cookie('uname','lisi',salt='hello',path='/abc/')
    return response


def getCookieInfo(request):
    # if 'uname' in request.COOKIES:
    #     return HttpResponse(request.COOKIES['uname'])
    uname = request.get_signed_cookie('uname','lisi',salt='hello')
    return HttpResponse('value:%s'%uname)
