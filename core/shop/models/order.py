from django.db import models
from ..services import OrderService
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    buyer_id = models.ForeignKey('account.CustomUser', on_delete=models.PROTECT)
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    delivery_date = models.DateField(_('delivery date'), blank=True, null=True)
    post_track_code = models.CharField(_('post track code'), max_length=100, blank=True, null=True)
    total_fee = models.BigIntegerField(_('total fee'), blank=True, null=True)
    is_paid = models.BooleanField(_('is paid'), default=False)
    is_processed = models.BooleanField(_('is processed'), default=False)
    is_sent = models.BooleanField(_('is sent'), default=False)
    is_delivered = models.BooleanField(_('is delivered'), default=False)
    paid_date = models.DateTimeField(_('paid date'), blank=True, null=True)

    def __str__(self):
        return f'{self.buyer_id.__str__()} at : {self.created_date}'

    def calculate_total_fee(self):
        result = OrderService.total(self)
        return result

    def get_items(self):
        return OrderService.get_items(self)

    def pay(self, paid_date):
        self.is_paid = True
        self.paid_date = paid_date

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ('-created_date', 'is_processed')


class Item(models.Model):
    order_id = models.ForeignKey('shop.Order', verbose_name=_('order'), on_delete=models.CASCADE)
    product_id = models.ForeignKey('shop.Product', verbose_name=_('product'), related_name='products',
                                   on_delete=models.PROTECT)
    amount = models.IntegerField(_('amount'), default=0)

    @property
    def total(self):
        return self.product_id.price * self.amount

    def __str__(self):
        return f'{self.product_id.name}'

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
