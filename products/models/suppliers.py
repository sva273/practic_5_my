from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'suppliers'