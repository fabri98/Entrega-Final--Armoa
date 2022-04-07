from django.db import models
from django.db.models.fields.files import ImageField
import datetime
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

class Comentario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    comentario = models.TextField()
    date = models.DateField(datetime.date.today)

class ProjectUser(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    # image = ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)           

