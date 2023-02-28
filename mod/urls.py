from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('auth/register/', views.register, name="register"),
    path('auth/login/', views.login, name="login"),
    path('auth/main/', views.main, name="main")
]
