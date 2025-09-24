from django.db import models

from products.models.orders import Order
from products.models.products import Product

# Create your models here.

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f" {self.quantity} x {self.product.name} for {self.order}"

