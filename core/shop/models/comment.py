from django.db import models


class Comment(models.Model):
    author_id = models.ForeignKey('account.CustomUser', on_delete=models.PROTECT)
    product_id = models.ForeignKey('shop.Product', on_delete=models.PROTECT)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:60]
