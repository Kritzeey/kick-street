from django.shortcuts import redirect, render

from products.forms import ProductForm

def show_create_product(request):
    form = ProductForm(request.POST)

    if form.is_valid() and request.method == "POST":
        form.save()

        return redirect("main:show_main")
    
    context = { "form": form }

    return render(request, "create_product.html", context)
