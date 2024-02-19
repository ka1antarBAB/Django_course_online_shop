from django.contrib import messages
from django.utils.translation import gettext as _

from products.models import Product


class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        add a product to the cart if it exists
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            # self.cart[product_id]['quantity'] = quantity
            if 'quantity' in self.cart[product_id] and quantity != self.cart[product_id]['quantity']:
                self.cart[product_id]['quantity'] = quantity
        elif quantity != self.cart[product_id]['quantity']:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        messages.success(self.request, _('successfully added to cart'))

    def remove(self, product):
        """
        remove a product from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('remove from the cart'))
            self.save()

    def save(self):
        """
        Mark session as modified to save changes
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_object'] = product
        for item in cart.values():
            item['total_price'] = item['product_object'].price * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart)

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum(item["quantity"] * item['product_object'].price for item in self.cart.values())



