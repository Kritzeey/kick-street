from django.urls import path
from main.views import show_main, show_products_xml, show_products_json, show_product_xml_by_id, show_product_json_by_id
app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("xml/", show_products_xml, name="show_xml"),
    path("json/", show_products_json, name="show_json"),
    path("xml/<str:product_id>/", show_product_xml_by_id, name="show_xml_by_id"),
    path("json/<str:product_id>/", show_product_json_by_id, name="show_json_by_id"),
]
