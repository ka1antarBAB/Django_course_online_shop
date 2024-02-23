from django.shortcuts import render
from django.views import generic
# Create your views here.


class OrderListView(generic.TemplateView):
    template_name = 'orders/order_create.html'
