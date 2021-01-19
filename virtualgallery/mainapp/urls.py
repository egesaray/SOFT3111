from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('',views.home),
    path('loginPage/',views.loginPage,name='loginPage'),
    path('logoutPage/',views.logoutPage,name='logoutPage'),
    path('registerPage/',views.registerPage,name='registerPage'),
    path('galleries/',views.galleries ,name='galleries'),
    path('galleryname/<str:pk>',views.galleryname,name='galleryname'), #Specific gallery (will be rearranged)
    path('virtualtour/<str:pkv>',views.virtualtour ,name='virtualtour'),#GalleryName/VirtualTour (will be rearranged)
    path('uploadpage/',views.uploadpage ,name='uploadpage'), #User_UploadPage
    path('myaccount/',views.myaccount ,name='myaccount'), #User_My Account
    # path('index/',views.webgl ,name='webgl'),
    path('forgotpassword/',auth_views.PasswordResetView.as_view() ,name='forgotpassword'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view() ,name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view() ,name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view() ,name='password_reset_complete'),

]