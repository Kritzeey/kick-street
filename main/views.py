from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        "app_name": "Kick Street",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E",
    }

    return render(request, "main.html", context)
