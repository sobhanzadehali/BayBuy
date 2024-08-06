from rest_framework.viewsets import ModelViewSet
from shop.models import Order, Item
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from ..permissions import OrderPermission, OrderItemPermission
from ..serializers.order import OrderSerializer, ItemSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser, OrderPermission)
    queryset = Order.objects.all()


class OrderItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = (IsAdminUser, OrderItemPermission)
    queryset = Item.objects.all()
