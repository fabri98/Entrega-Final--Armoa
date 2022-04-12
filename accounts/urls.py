from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_request, register, edit,profile


urlpatterns = [
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='layout.html'), name="logout"),
    path('register/', register, name="register"),
    path('edit/', edit, name="edit"),
    path('profile/', profile, name="profile"), 
]