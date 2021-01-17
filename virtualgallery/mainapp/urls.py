from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('loginPage/',views.loginPage,name='loginPage'),
    path('logoutPage/',views.logoutPage,name='logoutPage'),
    path('registerPage/',views.registerPage,name='registerPage'),
    path('forgotpassword/',views.forgotpassword ,name='forgotpassword'),
    path('galleries/',views.galleries ,name='galleries'),
    path('galleryname/<str:pk>',views.galleryname,name='galleryname'), #Specific gallery (will be rearranged)
    path('virtualtour/<str:pkv>',views.virtualtour ,name='virtualtour'),#GalleryName/VirtualTour (will be rearranged)
    path('uploadpage/',views.uploadpage ,name='uploadpage'), #User_UploadPage
    path('myaccount/',views.myaccount ,name='myaccount'), #User_My Account
    path('index/',views.webgl ,name='webgl'),

]