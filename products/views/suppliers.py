from rest_framework import viewsets
from products.models.suppliers import Supplier
from products.serializers.suppilers import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer