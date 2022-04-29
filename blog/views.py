from audioop import reverse
from django.shortcuts import render, redirect
from .models import Post
from .forms import FormPost
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


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

# CRUD
@login_required
def posts(request):

    posts = Post.objects.all()
    return render(request, 'posts.html',{'posts': posts})   


def blog_detalle(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'blog_detalle.html',{'post': post})    

class EditarBlog(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = reverse_lazy('blog:posts')
    fields=['title','subtitle','author','description','imagen']

class BorrarBlog(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')

