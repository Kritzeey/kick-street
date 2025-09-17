from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField()
    price = models.IntegerField()
    stock = models.IntegerField()
    is_featured = models.BooleanField()

    def __str__(self):
        return self.name