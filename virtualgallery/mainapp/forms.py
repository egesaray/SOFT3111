from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email' ,'password1' , 'password2' ,'first_name' , 'last_name']


class ChangeInfoForm(ModelForm):
    class Meta:
        model = ourUser
        fields = ['username','email']


class uploadform(ModelForm):
    class Meta:
        model = Gallery
        fields = ['galleryName','galleryDescription','contactInfo']


class ImageUploadForm(ModelForm):
    class Meta:
        model = ArtWork
        fields = ['name','image']