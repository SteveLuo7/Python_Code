from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


def index_view(request):
    return render(request,'index.html')


def get_view(request):
    uname = request.GET.get('uname','hello')
    print(uname)

    return JsonResponse({'flag':True})


def post_view(request):
    uname = request.POST.get('uname','hello')
    print(uname)
    return JsonResponse({'flag':True})


class OnlyView(View):
    def get(self,requset):
        return render(requset,'only.html')


class Student:
    pass


def getInfo(request):
    sname = request.GET.get('sname','')
    stu = Student.objects.filter(sname=sname)
    flag = False
    if stu:
        flag = True

    return JsonResponse({'flag':flag})