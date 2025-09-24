from django.db import models

from products.models.customers import Customer


# Create your models here.


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')

    def __str__(self):
        return f"Order of {self.id} {self.customer}"

    class Meta:
        db_table = 'orders'
        verbose_name_plural = "Orders"
        ordering = ['-order_date',]
        get_latest_by = 'order_date'
