from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, BusquedaBlog
from .forms import FormPost
from django.contrib.auth.decorators import login_required


# def render_posts(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', {'posts': posts,'imagen': buscar_url_imagen})   

def post_id(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_id.html',{'post':post})   

@login_required
def formulario_post(request):
    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            nuevo_post = Post(
                title= data['title'],
                subtitle=data['subtitle'],
                author=data['author'],
                description=data['description'], 
                # date=data['date'],
                imagen=data['imagen'],
            )
        
            nuevo_post.save()
            return redirect('blog:posts') 
        else:    
            return render(request, 'crear_post.html',{'form':form})
    form = FormPost()        
    return render(request, 'crear_post.html',{'form':form})             

def busqueda_blog(request):
    blog_buscado = []
    dato = request.GET.get('partial_blog', None)

    if dato is not None:
        blog_buscado= Post.objects.filter(title__icontains=dato)
        
    buscador = BusquedaBlog()
    return render(request, 'busqueda_blog.html',{'buscador':buscador, 'blog_buscado': blog_buscado})    

# CRUD
def posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'posts.html',{'posts': posts})
    else:
        return redirect('login')     

def update(request, id):
    actualizar_post = Post.objects.get(id=id)
    if request.method == 'POST':
        
        form = FormPost(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            actualizar_post.title = data['title']
            actualizar_post.subtitle = data['subtitle']
            actualizar_post.author = data['author']
            actualizar_post.description = data['description']
            actualizar_post.imagen = data['imagen']
        
            actualizar_post.save()
            return redirect('blog:posts') 
        else:    
            return render(request, 'actualizar_post.html',{'form':form,'actualizar_post':actualizar_post})
    form = FormPost(
        initial = {
            'title':actualizar_post.title,
            'subtitle':actualizar_post.subtitle,
            'author':actualizar_post.author,
            'description':actualizar_post.description,
            'date':actualizar_post.date,
            'imagen':actualizar_post.imagen,
        }
    )        
    return render(request, 'actualizar_post.html',{'form':form,'actualizar_post':actualizar_post})  

def delete(request,id):
    eliminar_post= Post.objects.get(id=id)

    eliminar_post.delete()
    return redirect('blog:posts') 

def blog_detalle(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'blog_detalle.html',{'post': post})    

 