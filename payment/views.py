from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json

from django.conf import settings
from orders.models import Order


# Create your views here.


# fat model thin views
def payment_process_view(request):
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
        "callback_url": 'https://127.0.0.1:8000/payment/callback/',

    }
    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_date), headers=request_header)
    data = json.loads(res.text)
    authority = data['authority']

    order.zarinpal_authority = authority
    order.save()

    if 'errors' not in data or len(data['errors']) == 0:
        return redirect("https://sandbox.zarinpal.com/pg/StartPay/{authority}".format(authority=authority))
    else:
        return HttpResponse("errors: " + str(data['errors']))


def payment_callback_view(request):
    payment_authority = request.GET('Authority')
    payment_status = request.GET.get('Status')

    order = get_object_or_404(Order, zarinpal_authority=payment_authority)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10
    if payment_status == 'Ok':
        request_header = {
            'accept': 'application/json',
            'content-type': 'application/json',
        }

        request_data = {
            'merchant_id': settings.MERCHANT_ID,
            'amount': rial_total_price,
            'authority': payment_authority,
        }

    res = requests.post(
        url="https://sandbox.zarinpal.com/pg/v4/payment/verify.json",
        data=json.dumps(request_data),
        headers= request_header
    )

    if 'data' in res.json() and ('errors' not in res.json()["data"] or len(res.json()["data"]['errors']) == 0):
        data = res.json()["data"]
        payment_code = data["code"]
        if payment_code == 100:
            order.is_verified = True
            order.ref_id = data["ref_id"]
            order.zarinpal_data = data
            order.save()

            return HttpResponse("پرداخت شما با موفقیت ثبت شد !")
        elif payment_code == 101:
            return HttpResponse("پرداخت شما با موفقیت ثبت شده است (البته این تراکنش قبلا ثبت شده است.!)")

        else:
            error_code = res.json()["errors"]["code"]
            error_message = res.json()["errors"]["message"]
            return HttpResponse(f"{error_code} , {error_message} تراکنش ناموفق بود , ")





