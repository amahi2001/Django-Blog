from django.db import models

# Create your models here.

class Job(models.Model):

    #creating a image field, storing the image in the images folder
    image = models.ImageField(upload_to='images/')

    #creating a summary field
    summary = models.CharField(max_length=200)
    
