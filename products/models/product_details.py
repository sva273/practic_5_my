from django.db import models

from products.models.products import Product


# Create your models here.

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    description = models.TextField(null=True, blank=True)
    manufacturing_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    weight = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def __str__(self):
        return f"Details of {self.product.name}"