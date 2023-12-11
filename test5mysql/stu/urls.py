#coding=utf-8

from django.urls import path, include

from stu import views

urlpatterns = [
    path('',views.login_view),
    path('login/',views.tologin),
]
