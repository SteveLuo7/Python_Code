import os.path

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self,requset):
        return render(requset,'index.html')


def r1View(request):
    with open(os.path.join(os.getcwd(),'templates','r.html'),'rb') as fr:
        content = fr.read()
    t = Template(content)
    c = Context({'uname':'zhangsan'})
    renderStr =  t.render(c)
    return HttpResponse(renderStr)


def t1(request):

    return render(request,'t.html')