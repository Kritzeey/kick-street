import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

def show_register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Your account has been successfully created!")

            return redirect("users:show_login")
        
    context = { 
        "form": form,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }

    return render(request, "register.html", context)

def show_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            user = form.get_user()

            login(request, user)

            response = HttpResponseRedirect(reverse("main:show_main"))

            response.set_cookie("last_login", str(datetime.datetime.now()))

            return response
    else:
        form = AuthenticationForm(request)
    
    context = { 
        "form": form, 
        "last_login": request.COOKIES.get("last_login", "Never"),
    }

    return render(request, "login.html", context)

def show_logout(request):
    logout(request)

    response = HttpResponseRedirect(reverse("users:show_login"))

    response.delete_cookie("last_login")

    return response
