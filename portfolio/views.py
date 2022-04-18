from django.shortcuts import render
from .models import Avatar, Project, Comentario , ProjectUser
from accounts.models import UserAvatar



def home(request):
    # projects = Project.objects.all()
    if request.method == 'POST':
        return render(request, 'home.html',{})
    elif request.method == 'GET' and request.user.is_authenticated:                 
        return render(request, 'home.html',{})
    else:    
        return render(request, 'home.html')    

def cargar_comentario(request):
    lista_comentario = Comentario.objects.all()
    if request.method == 'POST':
        nuevo_comentario = Comentario(nombre=request.POST['nombre'], email=request.POST['email'], comentario=request.POST['comentario'], date=request.POST['date'])
        nuevo_comentario.save()
        return render(request, 'formulario_comentario.html',{'nuevo_comentario':nuevo_comentario,'lista_comentario': lista_comentario})

    return render(request, 'formulario_comentario.html',{'lista_comentario': lista_comentario})

def projecto_usuario(request):
    lista_projecto = ProjectUser.objects.all()
    nuevo_projecto = ''
    if request.method == 'POST':
        nuevo_projecto = ProjectUser(title=request.POST['title'], description=request.POST['description'], url=request.POST['url'])   
        nuevo_projecto.save()
        return render(request, 'projecto_usuario.html',{'nuevo_projecto': nuevo_projecto, 'lista_projecto':lista_projecto})

    return render(request, 'projecto_usuario.html',{'nuevo_projecto': nuevo_projecto, 'lista_projecto':lista_projecto})


def buscar_url_avatar(user):
    return UserAvatar.objects.filter(user=user)[0].avatar.url


def about(request):
    return render(request, 'about.html',{})    