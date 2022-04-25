from django.shortcuts import render
from accounts.models import UserAvatar


def home(request):

    if request.method == 'POST':
        return render(request, 'home.html',{})
    elif request.method == 'GET' and request.user.is_authenticated:                 
        return render(request, 'home.html',{})
    else:    
        return render(request, 'home.html')    


def buscar_url_avatar(user):
    return UserAvatar.objects.filter(user=user)[0].avatar.url


def about(request):
    return render(request, 'about.html',{})    