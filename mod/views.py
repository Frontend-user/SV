from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, WallPostForm
from .models import User, WallPost

from django.http import HttpResponse
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if not user_form.is_valid():
            return render(request, "mod/register.html", context={'form_errors': user_form.errors})
        if not user_form.cleaned_data['password'] == user_form.cleaned_data['password2']:
            return render(request, "mod/register.html", context={'password_error': 'НЕВЕРНЫЙ ПАРОЛЬ'})
        if User.objects.filter(email=user_form.cleaned_data["email"]).first():
            return render(request, "mod/register.html",
                          context={'same_email': 'ПОльзователь т таким мейлом уже существует!!'})

        name = user_form.cleaned_data["first_name"]
        last_name = user_form.cleaned_data["last_name"]
        password = user_form.cleaned_data["password"]
        email = user_form.cleaned_data["email"]
        user = User.objects.create_user(first_name=name, last_name=last_name, password=password, email=email)

        # return HttpResponse(f"<h2>Hello, {name}, {family_name}, <br>password is {password},<br> email is {mail}</h2>")
        return redirect('login')

    elif request.method == 'GET':
        return render(request, "mod/register.html")


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user_data = register(request)
        if form.is_valid():
            user = auth.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                auth.login(request, user)
                return redirect('main')
            else:
                return render(request, "mod/login.html", context={'email_error': 'НЕВЕРНЫЙ  EMAIL  ИЛИ ПАРОЛЬ'})
    elif request.method == 'GET':

        return render(request, "mod/login.html")
    # return render(request, "mod/login.html")


def index(request):
    return render(request, "mod/index.html")


@login_required
def main(request):
    if request.method == 'POST':
        form = WallPostForm(request.POST)
        all_posts = WallPost.objects.filter(user_id=request.user.id)
        if not form.is_valid():
            return render(request, "mod/main.html",
                          {'err': 'Пишите пост правильно!! ОН не может быть пустым или больше 500 символов!!!',
                           'posts': [p.dict() for p in all_posts]})
        text = form.cleaned_data["text"]
        title = form.cleaned_data['title']
        WallPost.objects.create(text=text, title=title, user_id=request.user.id)

    elif request.method == 'GET':
        pass

    all_posts = WallPost.objects.filter(user_id=request.user.id)
    all_users = User.objects.filter().exclude(id=request.user.id)
    return render(request, 'mod/main.html',
                  {'posts': [p.dict() for p in all_posts], 'users': [s.users_dict() for s in all_users]})


def post_del(request, wall_post_id):
    WallPost.objects.filter(id=wall_post_id).first().delete()
    return redirect('main')


def users(request):
    return redirect('main')

def friends(request):
    # return render(request, '/auth/friends/')
    return render(request, 'mod/friends.html')