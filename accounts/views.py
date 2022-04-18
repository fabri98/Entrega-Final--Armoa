from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, EditUser
from django.contrib.auth.decorators import login_required
from portfolio.views import buscar_url_avatar
from .models import UserAvatar
# Create your views here.
def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)

                return render(request, 'home.html', {'mensaje':'Se logeo correctamente!!'})
            else:

                return render(request, 'home.html', {'mensaje': 'Error, datos incorrectos!!'})
        else:

            return render(request, 'home.html', {'mensaje': 'Error, datos incorrectos!!'})
    
    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'layout.html', {'mensaje': f'Se creo el usuario {username}'})
        else:
            return render(request, 'register.html', {'form': form})   
    form = UserForm()
    return render(request, 'register.html', {'form': form})

@login_required
def edit(request):  
    mensaje = ''

    user_avatar_logued, _ = UserAvatar.objects.get_or_create(user=request.user)
    if request.method == 'POST':      
        form = EditUser(request.POST, request.FILES)
        request.user

        if form.is_valid():
            data = form.cleaned_data
            request.user.email = data.get('email')
            request.user.first_name = data.get('first_name','')
            request.user.last_name = data.get('last_name','')
            user_avatar_logued.avatar = data.get('avatar','')
            user_avatar_logued.link = data.get('link','')


            if data.get('password1') == data.get('password2') and len(data.get('password1'))>8:
                request.user.set_password(data.get('password1'))
            else:
                mensaje = 'No se modifico el password'    
            
            user_avatar_logued.save()
            request.user.save()

            return render(request, 'layout.html', {'mensaje': mensaje})
        else:
            return render(request, 'edit_user.html', {'form': form})   
    form = EditUser(
        initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'email':request.user.email,
            'username':request.user.username,
            'avatar':user_avatar_logued.avatar,
            'link':user_avatar_logued.link,
        }
    )
    return render(request, 'edit_user.html', {'form': form,'mensaje':''})

@login_required
def profile(request):
    return render(request, 'profile.html',{})