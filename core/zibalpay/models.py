from django.db import models


# Create your models here.

class Zibalpay(models.Model):
    createdAt = models.DateTimeField(blank=True, null=True)
    verifiedAt = models.DateTimeField(blank=True, null=True)
    cardNumber = models.CharField(max_length=11, blank=True, null=True)
    status = models.IntegerField()
    amount = models.PositiveBigIntegerField()
    refNumber = models.IntegerField(blank=True, null=True)
    wage = models.IntegerField()
    result = models.IntegerField()
    message = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.id}. createdAt: {self.createdAt}'

    class Meta:
        verbose_name = 'Zibalpay'
        verbose_name_plural = 'Zibalpay'
