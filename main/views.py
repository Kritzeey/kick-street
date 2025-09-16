from http.client import HTTPResponse
from django.shortcuts import render
from django.core import serializers
from main.models import Product

def show_main(request):
    context = {
        "title": "Kick St.",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
    }

    return render(request, "main.html", context)

def show_products_xml(request):
    products = Product.objects.all()

    data = serializers.serialize("xml", products)

    return HTTPResponse(data, content_type="application/xml")

def show_products_json(request):
    products = Product.objects.all()

    data = serializers.serialize("json", products)

    return HTTPResponse(data, content_type="application/json")

def show_products_xml_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)

        data = serializers.serialize("xml", product)

        return HTTPResponse(data, content_type="application/xml")
    except Product.DoesNotExist:
        return HTTPResponse(status=404)

def show_products_json_by_id(request, id):
    try:
        product = Product.objects.filter(pk=id)

        data = serializers.serialize("json", product)

        return HTTPResponse(data, content_type="application/json")
    except Product.DoesNotExist:
        return HTTPResponse(status=404)
