from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import models
from .forms import RegisterForm
from .forms import LoginForm
from .models import User
from django.contrib.auth import authenticate
from django.template import Context, Template

def register(request):
    if request.method == 'POST':
        password_error = False
        user_form = RegisterForm(request.POST)
        if not user_form.is_valid():
            return HttpResponse('invalid')
        if not user_form.cleaned_data['password'] == user_form.cleaned_data['password2']:
            return render(request, "mod/register.html", context={'password_error': 'НЕВЕРНЫЙ ПАРОЛЬ'})
        if  User.objects.filter(mail=user_form.cleaned_data["email"]).first():

            return render(request, "mod/register.html", context={'same_email': 'НЕВЕРНЫЙ mail'})

            User.objects.filter(mail=form.cleaned_data["email"], password=form.cleaned_data["password"]).first()
            # return render(request, "mod/register.html")
        name = user_form.cleaned_data["name"]
        family_name = user_form.cleaned_data["family_name"]
        password = user_form.cleaned_data["password"]
        mail = user_form.cleaned_data["email"]
        user = User.objects.create(first_name=name, family_name=family_name, password=password, mail=mail)


        # return HttpResponse(f"<h2>Hello, {name}, {family_name}, <br>password is {password},<br> mail is {mail}</h2>")
        return redirect(login)

    elif request.method == 'GET':
        return render(request, "mod/register.html")


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(mail=form.cleaned_data["email"], password=form.cleaned_data["password"]).first()

            if user:

                return render(request, "mod/main.html", context={'user': user})
                # return redirect("main")
            else:
                return  render(request, "mod/login.html", context={'mail_error': 'НЕВЕРНЫЙ ПАРОЛЬ'})
    elif request.method == 'GET':

        return render(request, "mod/login.html")
    # return render(request, "mod/login.html")

def main(request):
    return render(request, "mod/main.html")

def index(request):
    return render(request, "mod/index.html")
