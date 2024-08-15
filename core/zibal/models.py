from django.db import models

# Create your models here.


from django.db import models


# Create your models here.

class Zibalpay(models.Model):
    createdAt = models.DateTimeField(blank=True, null=True, verbose_name='created at')
    verifiedAt = models.DateTimeField(blank=True, null=True, verbose_name='verified at')
    cardNumber = models.CharField(max_length=11, blank=True, null=True, verbose_name='card number')
    status = models.IntegerField(verbose_name='status')
    amount = models.PositiveBigIntegerField(verbose_name='amount')
    refNumber = models.IntegerField(blank=True, null=True, verbose_name='reference number')
    wage = models.IntegerField(verbose_name='wage')
    result = models.IntegerField(verbose_name='result')
    message = models.CharField(max_length=25, verbose_name='message')

    def __str__(self):
        return f'{self.id}. createdAt: {self.createdAt}'

    class Meta:
        verbose_name = 'Zibalpay'
        verbose_name_plural = 'Zibalpay'
