from django.shortcuts import render, get_object_or_404
from .models import Post, BusquedaBlog

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_id(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_id.html',{'post':post})   

def formulario_post(request):
    if request.method == 'POST':
        nuevo_post = Post(title=request.POST['title'], description=request.POST['description'], date=request.POST['date'])
        nuevo_post.save()
        return render(request, 'crear_post.html',{'nuevo_post':nuevo_post})  
    
    return render(request, 'crear_post.html',{})     

def busqueda_blog(request):
    blog_buscado = []
    dato = request.GET.get('partial_blog', None)

    if dato is not None:
        blog_buscado= Post.objects.filter(title__icontains=dato)
        
    buscador = BusquedaBlog()
    return render(request, 'busqueda_blog.html',{'buscador':buscador, 'blog_buscado': blog_buscado})    