from django.db import models, IntegrityError
from django.utils.translation import gettext_lazy as _


class Coupon(models.Model):
    seller_id = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    coupon_code = models.CharField(_('Coupon Code'), max_length=20, unique=True)
    percent = models.PositiveIntegerField(_('percent'), default=0)
    expiration_date = models.DateTimeField(_('expiration date'))
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return f'{self.coupon_code}, {self.description[:30]}'

    class Meta:
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')


class CouponBuyerProduct(models.Model):
    coupon_id = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    product_id = models.ForeignKey('shop.Product', on_delete=models.CASCADE)

    def set_coupon(self, coupon_obj, buyer_list, product_obj):
        """
        sets coupon to given buyer list for a product
        :param coupon_obj: Coupon object
        :param buyer_list:
        :param product_obj:
        :return: None
        """
        for item in buyer_list:
            try:
                self.objects.create(coupon_id=coupon_obj, buyer_id=item, product_id=product_obj)
            except IntegrityError:
                raise Exception('something went wrong while setting coupon for users')

    def __str__(self):
        return f'{self.buyer_id.phone}, {self.product_id}'

    class Meta:
        unique_together = ('coupon_id', 'buyer_id', 'product_id')
