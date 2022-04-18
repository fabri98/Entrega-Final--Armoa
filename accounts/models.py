from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAvatar(models.Model):
    avatar = models.ImageField(upload_to='avatares', blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    link = models.URLField(null=True)
