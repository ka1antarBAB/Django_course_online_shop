from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

from products.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_("last name"))
    phone_number = PhoneNumberField(verbose_name=_('phone number'))
    address = models.CharField(max_length=500, verbose_name=_("address"))

    date_ordered_created = models.DateTimeField(auto_now_add=True)
    date_ordered_modified = models.DateTimeField(auto_now=True)

    order_notes = models.CharField(max_length=500, blank=True, verbose_name=_("order notes"))

    zarinpal_authority = models.CharField(max_length=255, blank=True, verbose_name=_("authority"))
    zarinpal_ref_id = models.CharField(max_length=255, blank=True, verbose_name=_("ref_id"))
    zarinpal_data = models.TextField(blank=True)

    def __str__(self):
        return f'Order : {self.id}'

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    date_ordered_created = models.DateTimeField(auto_now_add=True)
    date_ordered_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order Item : {self.id} - {self.product} | Quantity : {self.quantity} | Price : {self.price}'
