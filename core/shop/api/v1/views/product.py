from rest_framework import viewsets, status, views
from rest_framework.permissions import IsAdminUser
from shop.api.v1.permissions import IsSellerOrReadOnly, IsAdminOrReadOnly
from shop.api.v1.serializers import ProductSerializer, CategorySerializer
from shop.models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    """
    product viewset
        list, retrive -> everyone
        C,U,D -> seller
    """
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser, IsSellerOrReadOnly]
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    category viewset,
    """
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
