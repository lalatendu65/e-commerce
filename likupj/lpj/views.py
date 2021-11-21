from os import name
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from lpj.models import *

# Create your views here.
def test(request):
    return render(request,'test.html')

def welcome(request):
    name='Liku'
    greet='is trying to get job in mnc'
    con={'kname':name,'kgreet':greet}
    return render(request,'respone.html',{'kcon':con})

def index(request):
    allproduct=product.objects.all()

    return render (request,'index.html',{'all':allproduct})

def about(request):
    return HttpResponse('we are at about')
def contact(request):
    return HttpResponse('we are at contact')
def tracker(request):
    return HttpResponse('we are at tracker')
def search(request):
    return HttpResponse('we are at search')
def ptview(request):
    return HttpResponse('we are at product')
def checkout(request):
    return HttpResponse('we are at checkout ')
