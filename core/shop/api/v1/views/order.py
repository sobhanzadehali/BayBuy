from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, schemas
from shop.models import Order, Item
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from ..permissions import OrderPermission, OrderItemPermission
from ..serializers import OrderSerializer, ItemSerializer


class OrderViewSet(ModelViewSet):
    """
    viewset of Order model
    """
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser, OrderPermission)
    queryset = Order.objects.all()


class OrderItemViewSet(ModelViewSet):
    """
    viewset of OrderItem model
    """
    serializer_class = ItemSerializer
    permission_classes = (IsAdminUser, OrderItemPermission)
    queryset = Item.objects.all()


class SellerOrdersAPIView(APIView):
    """
    views sold item to process to each seller
    """
    permission_classes = (IsAuthenticated,)
    schema = schemas.AutoSchema

    def get(self, request):
        queryset = Item.objects.filter(order_id__is_processed=False).filter(product_id__seller_id=request.user)
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

