from django.urls import path
from main.views import show_main, show_create_product

app_name="main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product/", show_create_product, name="show_create_product"),
]