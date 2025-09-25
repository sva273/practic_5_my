from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.models.customers import Customer
from products.serializers.customers import CustomerSerializer, CustomerCreateUpdateSerializer

class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


class CustomerDetailsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('first_name', 'last_name')
    filterset_fields = ['first_name', 'last_name']