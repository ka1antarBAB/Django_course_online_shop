from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

# Create your views here.
from cart.cart import Cart
from .forms import OrderForm
from . models import OrderItem


@login_required()
def order_create_view(request):
    form = OrderForm()
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, _('you can not continue with your cart because your cart is empty '))
        return redirect("products:list")
    if request.method == 'POST':
        form = OrderForm(request.POST)
        # order
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            # order item
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item["product_object"],
                                         quantity=item["quantity"],
                                         price=item["product_object"].price
                                         )
            cart.clear()
            request.user.first_name = order.first_name
            request.user.last_name = order.last_name
            request.user.save()
            messages.success(request, _('Your order has been successfully placed'))
    else:
        form = OrderForm()
    return render(request, 'orders/order_create.html', context={
        'form': form,

    })
