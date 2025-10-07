from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def show_main(request):
    featured_products = Product.objects.filter(is_featured=True)

    context = {
        "app_name": "Kick Street",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
        "products": featured_products,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }

    return render(request, "main.html", context)
