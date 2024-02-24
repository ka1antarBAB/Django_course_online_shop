from django import forms
from django.utils.translation import gettext as _

from orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'order_notes', ]
        widgets = {
            "address": forms.Textarea(attrs={'row': 2}),
            "order_notes": forms.Textarea(attrs={'rows': 5, 'cols': 50, 'placeholder': _('if you have any note Enter here please')}),
        }
