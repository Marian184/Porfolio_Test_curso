from django.db import models

# Create your models here.
class Job(models.Model):
    #puedo buscar en la pagina cuales son los atributos que le puedo dar a la parte
    #upload_to ----  django model fields
    image = models.ImageField(upload_to='images/') #this makes that all images created, will be storage inside MEDIA folder, images

    summary = models.CharField(max_length=200)