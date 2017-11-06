# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index1.html')
def temp(request):
    return render(request,'temp.html')
def details(request):
    return render(request, 'details.html')
def current_defines(request):
    return render(request,'current_defines.html')
def create_newdefine(request):
    return render(request,'create_newdefine.html')
def define_detail(request):
    return render(request,'define_detail.html')
def ajax_add(request,models):
    a = models.shuoyarStudent()
    return HttpResponse(a)
