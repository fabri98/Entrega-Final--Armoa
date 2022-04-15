from django.contrib import admin
from django.urls import path

from . import views

app_name='blog'

urlpatterns = [
    path('', views.posts, name='posts'),   
    path('<int:post_id>', views.post_id, name="post_id"),
    path('formulario-post/', views.formulario_post, name='formulario_post'),
    path('busqueda-blog/', views.busqueda_blog, name="busqueda_blog"),

    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('detail/<int:id>',views.blog_detalle, name="blog_detalle"),
    

    
]