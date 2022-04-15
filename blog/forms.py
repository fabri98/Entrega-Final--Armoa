import datetime
from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField

class FormPost(forms.Form):
    title = forms.CharField(max_length=100,label='Titulo')
    subtitle = forms.CharField(max_length=200,label='Subtitulo')
    author = forms.CharField(max_length=100,label='Nombre del creador')
    description = RichTextFormField(required=False,label='Texto del articulo')
    imagen = forms.ImageField(required=False,label='Imagen')
    # date = forms.DateField(label='Fecha')