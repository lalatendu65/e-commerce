from os import name
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from lpj.models import *
from math import ceil

# Create your views here.
def test(request):
    return render(request,'test.html')

def welcome(request):
    name='Liku'
    greet='is trying to get job in mnc'
    con={'kname':name,'kgreet':greet}
    return render(request,'respone.html',{'kcon':con})

def index(request):
    products=product.objects.all()
    print(products)
    n=len(products)
    nslides=n//4 + ceil((n/4)-(n//4))
    #params={'no_slides':nslides,'range':range(1,nslides),'product':products}
    allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides] ]
    params={'allprod':allprods}

    return render (request,'index.html',params)

def about(request):
    return render(request,'about.html')
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
