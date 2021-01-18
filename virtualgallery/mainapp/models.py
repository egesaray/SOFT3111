from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ourUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # relation with django's user # will be implemented later
    username = models.CharField(max_length=255,null=True)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Gallery(models.Model):
    galleryName = models.CharField(max_length=255,null=True)
    galleryDescription = models.TextField()
    contactInfo = models.CharField(max_length=500,null=True)
    ouruser = models.ForeignKey(ourUser,null=True,on_delete= models.CASCADE)

    def __str__(self):
        return self.galleryName


class ArtWork(models.Model):
    name = models.CharField(max_length=255,null=True)
    image = models.ImageField(null=True, blank=True)
    gallery = models.ForeignKey(Gallery,null=True,on_delete= models.CASCADE)

    # unitycoordinatesX = models.IntegerField(null=True, blank=True)
    # unitycoordinatesY = models.IntegerField(null=True, blank=True)
    # unitycoordinatesZ = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


#
# class VirtualTour(models.Model):
#     gallery = models.OneToOneField(Gallery, null=True, on_delete=models.CASCADE)
