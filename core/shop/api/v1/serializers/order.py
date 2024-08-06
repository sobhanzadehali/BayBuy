from rest_framework import serializers
from shop.models import Item, Order


class OrderSerializer(serializers.ModelSerializer):
    is_paid = serializers.BooleanField(read_only=True)
    paid_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        validated_data['buyer_id'] = self.context['request'].user
        return super().create(validated_data)


class ItemSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()

    class Meta:
        model = Item
        fields = '__all__'
