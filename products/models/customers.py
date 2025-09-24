from django.db import models

from products.models.addresses import Address


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='customers')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Customer of {self.first_name} {self.last_name}"

    class Meta:
        db_table = 'customers'
        ordering = ['-date_joined',]
        get_latest_by = 'date_joined'