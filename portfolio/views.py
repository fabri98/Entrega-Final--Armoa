from django.shortcuts import render
from .models import Project, Comentario , ProjectUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

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

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)

                return render(request, 'home.html', {'mensaje': f'Bienvenido {usuario}'})
            else:

                return render(request, 'home.html', {'mensaje': 'Error, datos incorrectos'})
        else:

            return render(request, 'home.html', {'mensaje': 'Error, formulario erroneos'})
    
    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'home.html', {'mensaje': f'Se creo el usuario {username}'})
        else:
            return render(request, 'register.html', {'form': form})   
    form = UserForm()
    return render(request, 'register.html', {'form': form})

