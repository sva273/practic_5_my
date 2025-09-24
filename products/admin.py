from django.contrib import admin
from .models import Category, Customer, Supplier, Address, Product, ProductDetail, Order, OrderItem

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_email", "phone_number")
    search_fields = ("name", "contact_email", "phone_number")
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "supplier", "price", "quantity", "article", "is_available")
    list_filter = ("category", "supplier", "is_available")
    search_fields = ("name", "article")
    ordering = ("category", "quantity")
    list_editable = ("price", "quantity", "is_available")

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number')
    search_fields = ("country", "city", "street", "house_number")
    ordering = ("country", "city", "street")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_joined', 'is_deleted', 'deleted_at',)
    search_fields = ("first_name", "last_name", "email", "phone_number",)
    ordering = ('-date_joined',)
    list_filter = ("is_deleted",)
    list_editable = ("is_deleted",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'customer')
    search_fields = ("customer__first_name", "customer__last_name", "customer__email")
    ordering = ('-order_date',)





