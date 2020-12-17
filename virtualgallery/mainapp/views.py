from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request,'mainapp/homepage.html')

def register(request):
    return render(request,'mainapp/register.html')

def forgotpassword(request):
    return render(request,'mainapp/forgotpassword.html')

def galleries(request):
    return render(request,'mainapp/galleries.html')

def galleryname(request):
    return render(request,'mainapp/galleryname.html')

def virtualtour(request):
    return render(request,'mainapp/virtualtour.html')

def uploadpage(request):
    return render(request,'mainapp/uploadpage.html')

def myaccount(request):
    return render(request,'mainapp/myaccount.html')

