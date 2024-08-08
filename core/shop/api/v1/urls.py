from django.urls import path
from rest_framework import routers
from shop.api.v1.views import ProductViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet, CouponViewSet, SetCouponViewSet

app_name = 'api-v1'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'items', OrderItemViewSet, basename='order-items')
router.register(r'coupons', CouponViewSet, basename='coupons')
router.register(r'set-coupons', SetCouponViewSet, basename='set-coupons')

urlpatterns = []

urlpatterns += router.urls
