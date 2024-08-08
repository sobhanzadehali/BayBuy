from django.db import models
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    author_id = models.ForeignKey('account.CustomUser',verbose_name=_('author'), on_delete=models.PROTECT)
    product_id = models.ForeignKey('shop.Product', verbose_name=_('product'), on_delete=models.PROTECT)
    body = models.TextField(verbose_name=_('comment body'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'))
    is_published = models.BooleanField(default=False, verbose_name=_('is published'))

    def publish(self):
        self.is_published = True
        self.save()

    def __str__(self):
        return self.body[:60]

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
