from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProductManager, self).get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_("Product Image"), upload_to="products/products_cover", blank=True, null=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField()
    price_daler = models.DecimalField(max_digits=4, decimal_places=2)

    objects = models.Manager()
    active_products_manager = ActiveProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args={self.pk})


# class ActiveCommentManager(models.Manager):
#     def get_queryset(self):
#         return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_START = [
        ('1', _('very bad')),
        ('2', _('bad')),
        ('3', _('not bad')),
        ('4', _('good')),
        ('5', _('very good')),

    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')

    body = models.TextField(verbose_name=_('text'))
    active = models.BooleanField(default=True)
    point = models.CharField(choices=PRODUCT_START, max_length=10, default=PRODUCT_START[0][0], verbose_name=_('point'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # active_comment_manager = ActiveCommentManager()
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('detail', args={self.product.id})
