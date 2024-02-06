from django.contrib import admin

from accounts.models import CustomUser
from products.models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('title', 'price', 'datetime_created', 'active',)

