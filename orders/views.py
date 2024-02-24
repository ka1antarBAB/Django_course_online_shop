from django.shortcuts import render
from django.views import generic
# Create your views here.
from .forms import OrderForm


def order_create_view(request):
    return render(request, 'orders/order_create.html', {'form': OrderForm()})
