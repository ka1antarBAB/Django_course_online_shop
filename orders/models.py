from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Order(models.Model):
    is_paid = models.BooleanField(default=False)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=500)

    date_ordered_created = models.DateTimeField(auto_now_add=True)
    date_ordered_modified = models.DateTimeField(auto_now=True)
