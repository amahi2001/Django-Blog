
from django.contrib import admin
from .models import Job

# Register your models here.

admin.site.register(Job) #we are now able to interact with our models on the /admin site
