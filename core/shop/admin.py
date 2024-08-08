from django.contrib import admin
from shop.models import Product, Category, Comment, ProductPictures, Order, Item, CouponBuyerProduct, Coupon


# Register your models here.

class CategoryInLine(admin.TabularInline):
    model = Category


class ProductPictureInLine(admin.TabularInline):
    model = ProductPictures
    extra = 5


class CouponBuyerProductInLine(admin.TabularInline):
    model = CouponBuyerProduct


class ItemInLine(admin.TabularInline):
    model = Item
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller_id', 'category_id', 'description', 'in_stock', 'price')
    list_filter = ('category_id', 'seller_id')
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductPictureInLine, CouponBuyerProductInLine]


class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_code', 'expiration_date')
    list_filter = ('coupon_code',)
    fieldsets = [(None, {'fields': ['seller_id', 'coupon_code', 'expiration_date', 'percent']})]


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInLine]
    list_display = ('buyer_id', 'created_date', 'is_paid')
    list_filter = ('buyer_id', 'is_paid')
    ordering = ('-created_date',)
    search_fields = ('buyer_id__fname', 'buyer_id__lname', 'buyer_id__phone')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'product_id', 'created_date', 'body')
    list_filter = ('created_date', 'product_id', 'author_id',)
    search_fields = (
        'author_id__fname',
        'author_id__lname',
        'author_id__phone',
        'product_id__name',
    )
    ordering = ('-created_date',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
