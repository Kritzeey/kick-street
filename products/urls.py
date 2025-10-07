from django.urls import path

from products.views import show_create_product, show_product_json_by_id, show_product_xml_by_id, show_products, show_products_json, show_products_xml

app_name = "products"

urlpatterns = [
    path("create/", show_create_product, name="show_create_product"),
    path("json/", show_products_json, name="show_json"),
    path("xml/", show_products_xml, name="xml"),
    path("json/<str:news_id>/", show_product_json_by_id, name="show_product_json_by_id"),
    path("xml/<str:news_id>/", show_product_xml_by_id, name="show_product_xml_by_id"),
    path("products/", show_products, name="show_products"),
]
