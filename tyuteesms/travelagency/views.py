from django.shortcuts import render,redirect
from travelagency.models import place
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def travelindex(request):
    p1=place()
    p1.destination='chennai'
    p1.price=800

    p2=place()
    p2.destination='odisha'
    p2.price=1500

    p3=place()
    p3.destination='Bangalor'
    p3.price=2000
    
    p4=place()
    p4.destination='Hydrabad'
    p4.price=2000

    p5=place()
    p5.destination='Goa'
    p5.price=3000

    p6=place()
    p6.destination='Kashmir'
    p6.price=5000

    dests=[p1,p2,p3,p4,p5,p6]
    return render(request,'travel agency/index.html',{'dests':dests})

