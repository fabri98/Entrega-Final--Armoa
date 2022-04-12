from django.shortcuts import render, get_object_or_404
from .models import Post, BusquedaBlog, ImagenPost
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
    imagen_post, _ = ImagenPost.objects.get_or_create(user=request.user)    
    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES)

        if form.is_valid():
            # request.user.title = form.cleaned_data['title']
            # request.user.subtitle = form.cleaned_data['subtitle']
            # request.user.author = form.cleaned_data['author']
            
            # request.user.description = form.cleaned_data['description']
            # request.user.date = form.cleaned_data['date']
            imagen_post.imagen = form.cleaned_data['imagen']
            # imagen_post = ImagenPost(imagen = request.FILES['imagen'], user=post_id)
            nuevo_post = Post(title=request.POST['title'],subtitle=request.POST['subtitle'],author=request.POST['author'],
            description=request.POST['description'], date=request.POST['date'])
        
            nuevo_post.save()
            imagen_post.save()
            return render(request, 'crear_post.html',{'nuevo_post':nuevo_post})
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

def posts(request):
    datos_post, _ = ImagenPost.objects.get_or_create(user=request.user)
    posts = Post.objects.all()

    return render(request, 'posts.html',{'posts': posts,'datos_post':datos_post}) 


