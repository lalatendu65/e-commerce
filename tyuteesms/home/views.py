from os import name
from django.shortcuts import render
from django.http import HttpResponse

from home.models import *

# Create your views here.



def viewbyloc(request):
   
   vmcount=int(request.GET['movies'])
   listactor=Actor.objects.filter(movies__iexact=vmcount)
   
           

   
   return render(request,'viewallres.html',{'actors':listactor})



def viewall(request):
   listactor=Actor.objects.all()
   return render(request,'viewallres.html',{'actors':listactor})


def home(request):
   return render(request,'home.html')
   
def insert(request):
   if request.method=='POST':
      name=request.POST['name']
      gen=request.POST['gen']
      location=request.POST['loc']
      mcount=int(request.POST['nom'])
      act1=Actor(1005,name,gen,location,)
      act1.movies=mcount
      act1.save()
      return render(request,'Actorresp.html',{'name':act1.name})
   else:
      return render(request,'Actorform.html')


def calculate(request):
   if request.method=='POST':
      n1=int(request.POST['n1'])
      n2=int(request.POST['n2'])
      add,sub,mul,div=n1+n2,n1-n2,n1*n2,n1/n2
      return render(request,'calculate.html',{'add':add,'sub':sub,'mul':mul,'div':div})
   else:
      return render(request,'calculateresp.html')

def welcome(request):
   # html='<html><body><h1>welcome to python django</h1><h2> first learn python </h2><p><B> This best webframe </B></p></body></html>'
    #return HttpResponse(html)
    Name='Liku'
    greet='is best for python'
    context={'cname':Name,'kgreet':greet}
    
    
    return render(request,'response.html',{'kcontext':context})
def setcookies(request):
   hresponse=render(request,'setcookies.html')
   hresponse.set_cookie('name','India')
   hresponse.set_cookie('sal',100000.34,max_age=86400)
   return hresponse
def getcookies(request):
   c1=request.COOKIES.get('name','guest')
   c2=request.COOKIES.get('sal',0)
   return render(request,'getcookies.html',{'c1':c1,'c2':c2})


def delcookies(request):
   hresponse=render(request,'delcookies.html')
   hresponse.delete_cookie('name')
   hresponse.delete_cookie('sal')
   return hresponse

def setsession(request):
   request.session['sname']='liku'
   request.session['ssal']=150000.23
   request.session['age']=25
   request.session.set_expiry(2*24*60*60)
   return render(request,'setsession.html')


def getsession(request):
   c1=request.session.get('sname')
   c2=request.session.get('ssal')
   sessiondata={'data1':c1,'data2':c2,'expdate':request.session.get_expiry_date(),'expage':request.session.get_expiry_age()}
   return render (request,'getsession.html',{'data':sessiondata})

def delsession(request):
   if 'ssal' in request.session:
      del request.session['ssal']
   request.session.flush()
   return render(request,'delsession.html')