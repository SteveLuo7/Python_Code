from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')

        if uname == 'zhangsan' and pwd == '123':
            return redirect('https://www.bing.com/',permanent=True)
    return HttpResponseRedirect('/stu/login/')