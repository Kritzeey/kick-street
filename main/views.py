import re
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url="/login")
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.filter(is_featured=True)
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        "title": "Kick St.",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
        "products": product_list,
        "last_login": request.COOKIES.get("last_login", "Never"),
        "current_user": request.user.username,
    }

    return render(request, "main.html", context)

@login_required(login_url="/login")
def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product
    }

    return render(request, "product_detail.html", context)

def show_create_product(request):
    form = ProductForm(request.POST)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)

        product_entry.user = request.user

        product_entry.save()

        return redirect("main:show_main")
    
    context = { "form": form }

    return render(request, "create_product.html", context)

def show_products_xml(request):
    products = Product.objects.all()

    data = serializers.serialize("xml", products)

    return HttpResponse(data, content_type="application/xml")

def show_products_json(request):
    products = Product.objects.all()

    data = serializers.serialize("json", products)

    return HttpResponse(data, content_type="application/json")

def show_product_xml_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)

        data = serializers.serialize("xml", product)

        return HttpResponse(data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_product_json_by_id(request, product_id):
    try:
        product = Product.objects.filter(pk=product_id)

        data = serializers.serialize("json", product)

        return HttpResponse(data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:show_login")
        
    context = { "form": form }

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
    
    context = { "form": form }

    return render(request, "login.html", context)

def show_logout(request):
    logout(request)

    response = HttpResponseRedirect(reverse("main:show_login"))

    response.delete_cookie("last_login")

    return response

def show_products(request):
    product_list = Product.objects.all();

    context = { "products": product_list }

    return render(request, "products.html", context)
