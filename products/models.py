from django.db import models
from django.shortcuts import reverse

from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField()
    price_daler = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    PRODUCT_START = [
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'not bad'),
        ('4', 'good'),
        ('5', 'very good'),

    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', )

    body = models.TextField()
    active = models.BooleanField(default=True)
    point = models.CharField(choices=PRODUCT_START, max_length=10, default=PRODUCT_START[0][0], blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


