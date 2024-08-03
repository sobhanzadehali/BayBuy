from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class ProductPictures(models.Model):
    product_id = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='products/%Y/%m/%d/')


class Product(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=255)
    seller_id = models.ForeignKey('account.CustomUser', verbose_name=_('seller'), on_delete=models.CASCADE)
    category_id = models.ForeignKey('shop.Category', verbose_name=_('category'), on_delete=models.CASCADE)
    price = models.BigIntegerField(_('price'), default=0)
    in_stock = models.BigIntegerField(_('available in stock'), default=0)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return self.name
