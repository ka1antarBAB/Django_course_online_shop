from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process_view, name='payment_process'),
    path('callback/', views.payment_callback_view, name='payment_callback'),
    path('process-sandbox/', views.payment_process_sandbox_view, name='payment_process_sandbox'),
    path('callback-sandbox/', views.payment_callback_sandbox_view, name='payment_callback_sandbox')

]
