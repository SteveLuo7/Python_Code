from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
def setSession(request):
    request.session['uname'] = 'zhangsan'
    # request.session.set_expiry(5)

    return HttpResponse('hello')


def getSession(request):
    uname = request.session.get('uname','')
    print (request.session.session_key)

    return HttpResponse(uname)

class User(object):
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd

import jsonpickle

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')

        if uname == 'zhangsan' and pwd == '123':
            user = User(uname,pwd)
            request.session['user'] = jsonpickle.dumps(user)
            return redirect('/stu/main/')
        else:
            return redirect('/stu/login/')



def main(request):
    user = request.session.get('user','')
    if user:
        u = jsonpickle.loads(user)
    uname = u.uname

    return HttpResponse('WELCOME YOUR LOGIN %s'%uname)


class IndexView(View):
    def get(self,request):
        return HttpResponse('hello GET request')
    def post(self,request):
        return HttpResponse('hello POST request')