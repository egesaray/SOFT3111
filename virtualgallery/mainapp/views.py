from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import  authenticate , login ,logout
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'mainapp/homepage.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('')

        context = {'form':form}
        return render(request,'mainapp/registerPage.html' , context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user= authenticate(request, username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect('')

        return render(request,'mainapp/loginPage.html')


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def forgotpassword(request):
    return render(request,'mainapp/forgotpassword.html')

def galleries(request):
    return render(request,'mainapp/galleries.html')

def galleryname(request):

    return render(request,'mainapp/galleryname.html')

def virtualtour(request):
    return render(request,'mainapp/virtualtour.html')


@login_required
def uploadpage(request):
    return render(request,'mainapp/uploadpage.html')


@login_required
def myaccount(request):
    return render(request,'mainapp/myaccount.html')

