from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail_view, name='detail_cart'),
    path('add/<int:product_id>', views.cart_add_view, name='cart_add'),
    path('remove/<int:product_id>', views.remove_from_cart, name='cart_remove'),

]
