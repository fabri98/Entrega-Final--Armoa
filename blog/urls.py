from django.contrib import admin
from django.urls import path

from . import views

app_name='blog'

urlpatterns = [
    path('', views.posts, name='posts'),   
    path('formulario-post/', views.formulario_post, name='formulario_post'),

    path('detail/<int:id>',views.blog_detalle, name="blog_detalle"),

    path('editar/<int:pk>', views.EditarBlog.as_view(template_name='editar_form.html'), name="editar_blog"),
    path('borrar/<int:pk>', views.BorrarBlog.as_view(template_name='borrar_confirm_delete.html'), name="borrar_blog"),

    
]