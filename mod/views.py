from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import models
from .forms import UserForm


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if not user_form.is_valivd():
            return HttpResponse('invalid')

        name = user_form.cleaned_data["name"]
        return HttpResponse(f"<h2>Hello, {name}</h2>")

    elif request.method == 'GET':
        return render(request, "mod/register.html")



def index(request):
    return render(request, "mod/index.html")
