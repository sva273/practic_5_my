from rest_framework import serializers

from products.models.orderitems import OrderItem
from products.serializers.orders import OrderSerializer
from products.serializers.products import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


    def validate_quantity(self, data):
        if data > 1000:
            raise serializers.ValidationError("Quantity must be less than 1000.")
        return data