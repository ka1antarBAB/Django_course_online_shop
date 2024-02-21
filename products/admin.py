from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from accounts.models import CustomUser
from products.models import Product, Comment


# Register your models here.


class ProductCommentsInline(admin.StackedInline):
    model = Comment
    fields = ('author', 'body', 'point', 'active',)
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'datetime_created', 'active',)
    inlines = [
        ProductCommentsInline,
    ]


@admin.register(Comment)
class ProductCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('product', 'datetime_created', 'active',)
