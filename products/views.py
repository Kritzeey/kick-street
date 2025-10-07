from django.shortcuts import get_object_or_404, redirect, render
from products.forms import ProductForm
from products.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()

        return redirect("main:show_main")
    
    context = { 
        "form": form,
        "app_name": "Kick Street",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
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

def show_products(request):
    products = Product.objects.all()

    context = { 
        "app_name": "Kick Street",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
        "products": products, 
    }

    return render(request, "products.html", context)

def show_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = { 
        "app_name": "Kick Street",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
        "product": product, 
    }
    
    return render(request, "product_detail.html", context)
