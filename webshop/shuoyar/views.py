# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from shuoyar.models import Author,Book,Publisher



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
def ajax_add(request):
    return HttpResponse(a)
def testmodel(request):
    # p = Publisher.objects.get(name = 'London')
    b =Book.objects.get(title = '魔戒')
    # b.title = '魔戒'
    # b.publisher = p
    # b.publication_date = '2017-04-05'
    a = Author.objects.get(name ='托尔金')
    b.authors.add(a)
    b.save()
    return HttpResponse('<h1>complect</h1>')
