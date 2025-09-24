from rest_framework import serializers
from products.models.addresses import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

