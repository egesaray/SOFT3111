from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('register/',views.register),
    path('forgotpassword/',views.forgotpassword),
    path('galleries/',views.galleries),
    path('galleryname/',views.galleryname), #Specific gallery (will be rearranged)
    path('virtualtour/',views.virtualtour),#GalleryName/VirtualTour (will be rearranged)
    path('uploadpage/',views.uploadpage), #User_UploadPage
    path('myaccount/',views.myaccount), #User_My Account
]