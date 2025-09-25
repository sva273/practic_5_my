from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.models.products import Product
from products.serializers.products import ProductSerializer, ProductCreateUpdateSerializer

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductDetail1UpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('name', 'category', 'price','supplier')
    filterset_fields = ['category', 'price']