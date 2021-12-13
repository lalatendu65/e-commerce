from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/travel')
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd1=request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd1)
        if user is not None:
            auth.login(request,user)
            return redirect('/travel')
        else:
            messages.error(request,'invalid credential')
            messages.info(request,'Either user id or password is incorrect')
            return redirect('../login/')

    else:
        return render(request,'accouncts/login.html')
def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        email=request.POST['email']
        
        if pwd1==pwd2:
            if User.objects.filter(username=uname).exists():
                messages.error(request,'username Already in use')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email id  Already in use')
            else:
                user=User.objects.create_user(username=uname,password=pwd1,email=email,first_name=fname,last_name=lname)
                user.save()
                messages.info(request,'user Registerd')
                return redirect('/travel')
        else:
            messages.error(request,'Both password and confirm password are not matching')
            return render(request,'accouncts/index.html')
    else:
        return render(request,'accouncts/index.html')