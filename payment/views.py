from django.shortcuts import get_object_or_404
import requests
import json

from django.conf import settings
from orders.models import Order


# Create your views here.


# fat model thin views
def payment_process(request):
    # get order id from session
    order_id = request.session.get('order_id')
    # get the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"

    request_header = {
        "accept": "application/json",
        "content-type": "application/json",
    }

    request_date = {
        "merchant_id": settings.ZARINPAL_MERCHANT_ID,
        "amount": rial_total_price,
        "description": f'#{order.id} : {order.user.first_name} {order.user.last_name}',
        "callback_url": '127.0.0.1:8000',

    }
    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_date), headers=request_header)

    print(res.json()['data'])

