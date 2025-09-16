from django.urls import path
from main.views import show_create_product, show_main, show_product, show_products_xml, show_products_json, show_product_xml_by_id, show_product_json_by_id
app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-product", show_create_product, name="show_create_product"),
    path("products/<str:product_id>", show_product, name="show_product"),
    path("xml/", show_products_xml, name="show_xml"),
    path("json/", show_products_json, name="show_json"),
    path("xml/<str:product_id>/", show_product_xml_by_id, name="show_xml_by_id"),
    path("json/<str:product_id>/", show_product_json_by_id, name="show_json_by_id"),
]
