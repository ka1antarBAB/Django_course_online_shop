from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _

from products.models import Product
from . cart import Cart
from . forms import AddToCartProductForm


# Create your views here.
def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item["product_update_quantity_form"] = AddToCartProductForm(initial={
            "quantity": item["quantity"],
            "ingredients": True,
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def cart_add_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data.get("quantity")
        cart.add(product, quantity, replace_current_quantity=cleaned_data.get("inplace"))

    return redirect('cart:detail_cart')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail_cart')


@require_POST
def cleared_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, _("your cart has been successfully removed from your cart"))
    else:
        messages.error(request, _("your cart is already empty"))

    return redirect('cart:detail_cart')
