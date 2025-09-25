from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from products.models.product_details import ProductDetail
from products.serializers.product_details import ProductDetailSerializer, ProductDetailCreateUpdateSerializer

class ProductDetailListCreateView(ListCreateAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer


class ProductDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer