from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import  authenticate , login ,logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def home(request):
    galle = Gallery.objects.last()
    artworks = ArtWork.objects.filter(gallery=galle)

    context ={'artworks': artworks , 'galle':galle}

    return render(request,'mainapp/homepage.html' , context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                ouser = ourUser(username=username ,first_name=first_name, last_name=last_name, email=email,user=user)
                ouser.save()
                return redirect('/')

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
                return redirect('/')

        return render(request,'mainapp/loginPage.html')


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def forgotpassword(request):
    return render(request,'mainapp/forgotpassword.html')

def galleries(request):
    gal = Gallery.objects.all()
    context = {'gal':gal }
    return render(request,'mainapp/galleries.html', context)

def galleryname(request,pk):
    gal = Gallery.objects.get(id=pk)
    art = ArtWork.objects.filter(gallery=gal)

    context={'gal': gal , 'art':art}
    return render(request,'mainapp/galleryname.html',context)

def virtualtour(request,pkv):
    gal = Gallery.objects.get(id=pkv)
    arts = ArtWork.objects.filter(gallery=gal)

    context = {'gal': gal, 'arts': arts}
    return render(request,'mainapp/virtualtour.html',context)

@login_required
def uploadpage(request):
    ruser = request.user.ouruser
    form = uploadform(request.POST)
    if request.method =='POST':
        form = uploadform(request.POST)
        if form.is_valid():
            galName = request.POST['galleryName']
            galDescp = request.POST['galleryDescription']
            continfo = request.POST['contactInfo']
            Gal = Gallery(galleryName=galName,galleryDescription=galDescp,contactInfo=continfo,ouruser=ruser)
            Gal.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'mainapp/uploadpage.html',context)

@login_required
def myaccount(request):

    ruser = request.user.ouruser

    mygals = Gallery.objects.filter(ouruser=ruser)

    form = ChangeInfoForm(instance=ruser)
    formi = PasswordChangeForm(data=request.POST, user=request.user)
    if request.method == 'POST':
        form = ChangeInfoForm(request.POST, instance=ruser)
        formi = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid() and formi.is_valid() :
            form.save()
            formi.save()
            return redirect('/')

    context = {'form': form , 'formi':formi , 'mygals':mygals}
    return render(request,'mainapp/myaccount.html', context)

def webgl(request):
    return render(request,'virtualtour/index.html')
