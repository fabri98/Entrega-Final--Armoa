from os import link
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_text = {k: '' for k in fields}


class EditUser(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(),required=False)
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput(), required=False)
    first_name = forms.CharField(label="Nombre",max_length=20,required=False)
    last_name = forms.CharField(label="Apellido",max_length=20)
    avatar = forms.ImageField(required=False)
    link = forms.URLField(required=False)
      
        