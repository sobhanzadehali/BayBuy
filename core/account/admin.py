from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser, SellerInfo
from .forms import CustomUserChangeForm, CustomUserCreationForm
from shop.admin import CouponBuyerProductInLine


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('phone', 'is_staff', 'is_superuser', 'is_active', 'is_seller',)
    list_filter = ('phone', 'fname', 'is_superuser', 'is_active', 'is_seller')
    fieldsets = [
        (None, {'fields': ['phone', 'password', 'fname', 'lname', 'date_of_birth', 'postal_code', 'address']}),
        ('permissions', {'fields': ['is_staff', 'is_superuser', 'is_active', 'is_seller']})
    ]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "phone", "password1", "password2", 'fname', 'lname', "is_staff",
                "is_active", "is_seller", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ('phone', 'fname', 'lname')
    ordering = ('phone',)
    inlines = (CouponBuyerProductInLine,)


class StackedUserInline(admin.StackedInline):
    model = CustomUser


class SellerInfoAdmin(admin.ModelAdmin):
    model = SellerInfo
    list_display = ('seller_id', )
    list_filter = ('seller_id',)
    search_fields = ('seller_id',)
    ordering = ('seller_id',)
    fieldsets = [
        (None, {'fields': ('seller_id', 'video', 'id_card', 'id_number',)}),
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SellerInfo, SellerInfoAdmin)
