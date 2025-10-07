from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from products.forms import ProductForm
from products.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def show_create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        new_product = form.save(commit=False)

        new_product.user = request.user

        new_product.save()

        return redirect("main:show_main")
    
    context = { 
        "form": form,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }

    return render(request, "create_product.html", context)

def show_products_json(request):
    products = Product.objects.all()

    data = serializers.serialize("json", products)

    return HttpResponse(data, content_type="application/json")

def show_products_xml(request):
    products = Product.objects.all()

    data = serializers.serialize("xml", products)

    return HttpResponse(data, content_type="application/xml")

def show_product_json_by_id(request, product_id):
    product = Product.objects.get(pk=product_id)

    data = serializers.serialize("json", [product])

    return HttpResponse(data, content_type="application/json")

def show_product_xml_by_id(request, product_id):
    product = Product.objects.get(pk=product_id)

    data = serializers.serialize("xml", [product])

    return HttpResponse(data, content_type="application/xml")

@login_required(login_url="/login")
def show_products(request):
    products = Product.objects.all()

    context = { 
        "products": products, 
        "last_login": request.COOKIES.get("last_login", "Never"),
    }

    return render(request, "products.html", context)

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = { 
        "product": product,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }
    
    return render(request, "product_detail.html", context)

def show_edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()

        return redirect("main:show_main")
    
    context = { 
        "form": form,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }

    return render(request, "edit_product.html", context)

def show_delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    product.delete()
    
    return HttpResponseRedirect(reverse("main:show_main"))
