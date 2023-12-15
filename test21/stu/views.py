from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index_view(request):
    l = ['a1','a2','a3']

    d = {'k1':'v1','k2':'v2'}

    return render(request,'index.html',{'uname':'zhangsan','l':l, 'd':d,
                                        'now':datetime.today()})


def f1(request):
    return render(request,'f.html',{'num':10,'str1':'hello'})


def f2(request):
    str1 = '#### SETTING URL'
    str2 = 'happyholiday'
    return render(request,'f2.html',{'str1':str1,'str2':str2,})