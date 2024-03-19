import os.path

from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from .models import UserData
from django.http import HttpResponse
from django.http import Http404
from .models import *
from django.contrib.auth import authenticate, login
from .models import UserData
# from .models import UserData_0
from django.contrib import auth

import re
# Create your views here.
from django.shortcuts import render
flag=0
def home(request):
    return render(request,'Home.html')

def home1(request):
    return render(request,'Home1.html')

def insights(request):
    return render(request,'Insights.html')

def login_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        x=auth.authenticate(email=email,password=password)
        print(email, password)
        if x is None:
            return redirect('loginpage')
        else:
            return redirect('home1')
            # messages.error(request, 'Please register yourself!')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
            # name = request.POST['name']
            username = request.POST['username']
            #contact= request.POST['contact']
            email = request.POST['email']
            password = request.POST['password']
            print(username, email, password)
            if UserData.objects.filter(username=username).exists():
                # print("User is already taken")
                messages.error(request, 'This username is alrady taken')
                return redirect('registrationpage' )
            elif UserData.objects.filter(email=email).exists():
                messages.error(request,"Email is already taken")
                return redirect('registrationpage')
            else:
                students = UserData(username=username, email=email, password=password)
                students.save()
                messages.success(request,"register succesfully")
    return render(request,'registration.html')



def ask_doubt(request):
    return render(request,'askdoubt.html')
# Create your views here.

def dashboard(request):
    return render(request,'Dashboard.html')

def placement(request):
    context = {'file': UserData.objects.all()}
    #placement = UserData.objects.all()
    #data = {
     #   'placement' : placement
    #}
    return  render(request,'placement.html',context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/file")
            response['Content-Disposition'] = 'inline;filename=' +os.path.basename(file_path)
            return response
    raise Http404


