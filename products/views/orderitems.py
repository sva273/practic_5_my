from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from products.models.orderitems import OrderItem
from products.serializers.orderitems import OrderItemSerializer, OrderItemCreateUpdateSerializer


class OrderItemListCreateView(ListCreateAPIView):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer


class OrderItemDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer