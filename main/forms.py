from django.forms import ModelForm
from main.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "brand", "description", "thumbnail", "price", "stock", "is_featured"]