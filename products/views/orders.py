from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.models.orders import Order
from products.serializers.orders import OrderSerializer, OrderCreateUpdateSerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer


class OrderDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer