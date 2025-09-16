from django.shortcuts import redirect, render

from main.forms import ProductForm

def show_main(request):
    context = {
        "title": "Kick St.",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E"
    }

    return render(request, "main.html", context)

def show_create_product(request):
    form = ProductForm(request.POST)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    
    context = {"form": form}

    return render(request, "create_product.html", context)