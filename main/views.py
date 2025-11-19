from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required
import requests

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

def proxy_image(request):
    image_url = request.GET.get("url")
    if not image_url:
        return HttpResponse("No URL provided", status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get("Content-Type", "image/jpeg")
        )
    except requests.RequestException as e:
        return HttpResponse(f"Error fetching image: {str(e)}", status=500)
