from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


# Register your models here.


class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    fields = ('order', 'product', 'quantity', 'price', )
    extra = 1


@admin.register(Order)
class OrderItemAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    model = Order
    list_display = ('user', 'first_name', 'last_name', 'phone_number', 'date_ordered_created', 'is_paid',)
    inlines = [OrderItemInLine]


@admin.register(OrderItem)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price',)
