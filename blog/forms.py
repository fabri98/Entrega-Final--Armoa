import datetime
from django import forms
from django.contrib.auth.models import User

class FormPost(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    imagen = forms.ImageField(required=False)
    date = forms.DateField()