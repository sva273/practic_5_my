from rest_framework import serializers
from products.models.products import Product
from products.serializers.categories import CategorySerializer
from products.serializers.suppilers import SupplierSerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'