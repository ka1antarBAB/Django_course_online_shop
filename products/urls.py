from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('comment/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create'),

]
