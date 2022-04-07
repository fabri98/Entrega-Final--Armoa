from django.shortcuts import render
from .models import Avatar, Project, Comentario , ProjectUser



def home(request):
    # projects = Project.objects.all()
    if request.method == 'POST':
        return render(request, 'layout.html',{'user_avatar': buscar_url_avatar(request.user)})
    elif request.method == 'GET' and request.user.is_authenticated:                 
        return render(request, 'layout.html',{'user_avatar': buscar_url_avatar(request.user)})
    else:    
        return render(request, 'layout.html')    

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
    return Avatar.objects.filter(user=user)[0].imagen.url