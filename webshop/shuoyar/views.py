# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def temp(request):
    return render(request,'temp.html')
def details(request):
    return render(request, 'details.html')
def ajax_add(request):
    a = "helloworld"
    return HttpResponse(a)
