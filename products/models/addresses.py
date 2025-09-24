from django.db import models

# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=6)

    def __str__(self):
        return f"Address of {self.country} {self.city} {self.street} {self.house_number}"

    class Meta:
        db_table = 'addresses'
        verbose_name_plural = "Addresses"