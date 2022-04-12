from django.db import models
import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, null=True)
    description = models.TextField()
    author = models.CharField(max_length=100, default=True)
    date = models.DateField(datetime.date.today)
    

    def __str__(self):
        return f'{self.title} - Fecha: {self.date}'


class ImagenPost(models.Model):        
    imagen = models.ImageField(upload_to='blog/images', blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class BusquedaBlog(models.Model):
    partial_blog= models.CharField(max_length=100)   
    