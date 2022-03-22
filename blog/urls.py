from django.contrib import admin
from django.urls import path
from .views import render_posts, post_id, formulario_post, busqueda_blog

app_name='blog'

urlpatterns = [
    path('', render_posts, name='posts'),   
    path('<int:post_id>', post_id, name="post_id"),
    path('formulario-post/', formulario_post, name='formulario_post'),
    path('busqueda-blog', busqueda_blog, name="busqueda_blog")
]