from django.shortcuts import render
from products.models import Product

def show_main(request):
    featured_products = Product.objects.filter(is_featured=True)

    context = {
        "app_name": "Kick Street",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
        "products": featured_products,
    }

    return render(request, "main.html", context)
