from django.urls import path

from products.views import show_create_product


app_name = "products"

urlpatterns = [
    path("create/", show_create_product, name="show_create_product")
]
