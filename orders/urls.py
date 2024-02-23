from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.OrderListView.as_view(), name='order_detail'),

]
