from django.shortcuts import render

def show_main(request):
    context = {
        "title": "Kick St.",
        "name": "Valerian Hizkia Emmanuel",
        "class": "PBP E"
    }

    return render(request, "main.html", context)