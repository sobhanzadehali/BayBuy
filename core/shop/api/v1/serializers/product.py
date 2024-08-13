from rest_framework import serializers
from account.api.v1.serializers.user import CustomUserSerializer
from shop.models import Product, ProductPictures, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    def validate(self, attrs):
        if attrs.get('seller_id') != self.context.get('request').user:
            raise serializers.ValidationError('authenticated user and product owner do not match')
        if not attrs.get('seller_id').is_seller:
            raise serializers.ValidationError('user has not permission to create product, become seller first.')
        return super().validate(attrs)

    def create(self, **validated_data):
        validated_data['seller_id'] = self.context.get('request').user
        return super().create(validated_data)

    class Meta:
        model = Product
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ProductPicturesSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(source='picture')
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductPictures
        fields = '__all__'

    def create(self, validated_data):
        pics = ProductPictures.objects.filter(product_id=validated_data['product'])
        if len(pics) <= 4:
            return super().create(validated_data)
        else:
            raise serializers.ValidationError(
                'product pictures can only have up to five images'
            )
