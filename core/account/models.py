from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(_('phone number'), max_length=11, unique=True)
    fname = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    lname = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    address = models.CharField(_('address'), max_length=100, blank=True, null=True)
    balance = models.BigIntegerField(_('Balance'), default=0)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active status'), default=True)
    is_seller = models.BooleanField(_('is seller'), default=False)
    is_verified = models.BooleanField(_('is verified'), default=False)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    postal_code = models.CharField(_('postal code'), max_length=20, blank=True, null=True)
    joined_date = models.DateField(_('date of joining'), auto_now_add=True)
    updated_date = models.DateField(_('date of update'), auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        if self.fname and self.lname:
            return f'{self.fname} {self.lname}'
        else:
            return self.phone

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class SellerInfo(models.Model):
    seller_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller_info')
    video = models.FileField(upload_to='seller/videos/')
    id_card = models.ImageField(upload_to='seller/cards/')
    id_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.id_number

    class Meta:
        verbose_name = _('sellers info')
        verbose_name_plural = _('sellers info')
