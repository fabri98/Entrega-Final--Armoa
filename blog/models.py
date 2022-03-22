from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)

    def __str__(self):
        return f'{self.title} - Fecha: {self.date}'

class BusquedaBlog(models.Model):
    partial_blog= models.CharField(max_length=100)   
    