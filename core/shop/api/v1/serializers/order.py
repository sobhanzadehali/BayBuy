from rest_framework import serializers
from shop.models import Item, Order


class OrderSerializer(serializers.ModelSerializer):
    is_paid = serializers.BooleanField(read_only=True)
    paid_date = serializers.DateTimeField(read_only=True)
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        try:
            return obj.get_items
        except:
            raise serializers.ValidationError("order has no items yet")

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        validated_data['buyer_id'] = self.context['request'].user
        return super().create(validated_data)


class ItemSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
