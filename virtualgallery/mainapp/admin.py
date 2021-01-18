from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(ourUser)
admin.site.register(Gallery)
# admin.site.register(VirtualTour)
admin.site.register(ArtWork)