from django.http import HttpResponse
from django.shortcuts import render

from stu.models import Student
from test14.settings import MEDIA_ROOT


# Create your views here.
def upload_view(request):

    return render(request,'upload.html')


def toupload_view(request):
    #   get request method
    sname = request.POST.get('sname')
    photo = request.FILES.get('photo')

    #   save in database
    student = Student.objects.create(sname=sname,photo=photo)

    if student:
        return HttpResponse('Upload Success')
    return HttpResponse('Upload Failed')


    return HttpResponse('%s,%s'%(sname,photo))


def showall(request):
    students = Student.objects.all()

    return render(request,'show.html',{'students' : students})

#   QuickView effect
def download1(request):
    #   images/xx.jpg
    photo = request.GET.get('photo')
    filename = photo[photo.rindex('/') + 1:]

    #   get the file path
    import os
    filepath = os.path.join(MEDIA_ROOT,photo)

    with open(filepath,'rb') as fr:
        content = fr.read()

    response = HttpResponse(content)
    response['content-type'] = 'image/jpg'

    response['content-disposition'] = 'attachment;filename='+filename
    return response