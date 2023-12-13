from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def query_view(request):
#     return HttpResponse('Hello my friend')


def index_view(request):
    m = request.method
    path = request.path
    scheme = request.scheme
    print('request method: {}'.format(m))
    print('request path: {}'.format(path))
    print('request scheme: {}'.format(scheme))
    for k,v in request.META.items():
        print(k, ':', v)
    return HttpResponse('request')