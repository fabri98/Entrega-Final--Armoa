from django.db import models
import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, null=True)
    description = RichTextField(blank=True,null=True)
    author = models.CharField(max_length=100, default=True)
    date = models.DateField(default=datetime.date.today)
    imagen = models.ImageField(upload_to='blog/images', blank=True,null=True)
    

    def __str__(self):
        return f'{self.title} - Fecha: {self.date}'


class BusquedaBlog(models.Model):
    partial_blog= models.CharField(max_length=100)   
    