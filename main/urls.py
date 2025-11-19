from django.urls import path
from main.views import proxy_image, show_main

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("proxy-image/", proxy_image, name="proxy_image"),
]
