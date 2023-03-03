from django.contrib import admin
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/register/', views.register, name="register"),
    path('auth/login/', views.login, name="login"),
    path('auth/logout/', views.logout_view, name="logout"),

    path('auth/main/', views.main, name="main"),
    path('auth/wall_post/delete/<int:wall_post_id>/', views.post_del, name="post_delete"),

    path('users/list/', views.users_list, name='users_list'),
    path('users/friend_add/<int:friend_id>/', views.friend_add, name='friend_add')

]
