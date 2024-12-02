from django.urls import path
from .views import render_register, render_login, register_user, user_login, user_logout

urlpatterns = [
    # HTML rendering views
    path('render/register/', render_register, name='render_register'),
    path('render/login/', render_login, name='render_login'),
    
    # API endpoints
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
