from rest_framework import serializers
import re

from products.serializers.addresses import AddressSerializer
from products.models.customers import Customer


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['date_joined', 'is_deleted', 'deleted_at']


class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    def validate_phone_number(self, value):
        if not re.match(r'^\+?\d{10,15}$', value):
            raise serializers.ValidationError('Phone number must be entered in the format, between 10-15')
        return value