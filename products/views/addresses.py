from rest_framework import viewsets
from products.models.addresses import Address
from products.serializers.addresses import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer