from django.db import models
from django.utils.translation import gettext_lazy as _


class Coupon(models.Model):
    coupon_code = models.CharField(_('Coupon Code'), max_length=20, unique=True)
    percent = models.PositiveIntegerField(_('percent'), default=0)
    expiration_date = models.DateField(_('expiration date'))
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return f'{self.coupon_code}, {self.description[:30]}'


class CouponBuyerProduct(models.Model):
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    product_id = models.ForeignKey('shop.Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.buyer_id.phone}, {self.product_id}'

