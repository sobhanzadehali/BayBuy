from rest_framework import permissions

from shop.models import Order, Item


class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Allows access only to product seller.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.is_seller and obj.seller_id == request.user.id:
            return True


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    only allows Admin to manage Object.
    others only have Read Only access.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        else:
            return False


class OrderPermission(permissions.BasePermission):
    """
    Allows access only to product buyer and superuser.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            view.queryset = Order.objects.filter(buyer_id=request.user)
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.buyer_id == request.user:
            return True
        else:
            return False


class OrderItemPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            view.queryset = Item.objects.filter(order_id__buyer_id=request.user)
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.order_id.buyer_id == request.user:
            return True
        else:
            return False
