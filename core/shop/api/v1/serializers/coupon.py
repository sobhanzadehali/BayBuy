from rest_framework import serializers
from shop.models import Coupon, CouponBuyerProduct


class CouponSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if len(attrs.get('coupon')) <= 3:
            raise serializers.ValidationError(
                "coupon code must be at least 3 characters long"
            )
        if not attrs.get('expiration_date'):
            raise serializers.ValidationError("expiration_date must be set")
        return super().validate(attrs)

    def create(self, **validated_data):
        validated_data['seller_id'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Coupon
        fields = '__all__'


class SetCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponBuyerProduct
        fields = '__all__'
