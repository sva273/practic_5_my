from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name_plural = "Categories"
        ordering = ['name']