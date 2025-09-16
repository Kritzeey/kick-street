from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    context = {
        "title": "Kick St.",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
    }

    return render(request, "main.html", context)

def show_create_product(request):
    form = ProductForm(request.POST)

    if form.is_valid() and request.method == "POST":
        form.save()

        return redirect("main:show_main")
    
    context = {"form": form}

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
