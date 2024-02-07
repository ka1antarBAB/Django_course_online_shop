from django.contrib import admin

from accounts.models import CustomUser
from products.models import Product, Comment
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'datetime_created', 'active',)


@admin.register(Comment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'datetime_created', 'active',)
