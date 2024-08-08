from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from shop.api.v1.serializers.coupon import CouponSerializer, SetCouponSerializer

from shop.models import Coupon, CouponBuyerProduct


class CouponViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CouponSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Coupon.objects.all()
        if user.is_seller:
            return Coupon.objects.filter(seller_id=user)


class SetCouponViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SetCouponSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CouponBuyerProduct.objects.all()
        if user.is_seller:
            return CouponBuyerProduct.objects.filter(coupon_id__seller_id=user)
