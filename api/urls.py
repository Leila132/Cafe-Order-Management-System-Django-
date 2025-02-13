from django.urls import path
from .views import DishListAPI, DishDetailAPI, OrderListAPI, OrderDetailAPI

urlpatterns = [
    path('dishs/', DishListAPI.as_view(), name='dish-list-api'),
    path('dishs/<int:pk>/', DishDetailAPI.as_view(), name='dish-detail-api'),
    path('orders/', OrderListAPI.as_view(), name='order-list-api'),
    path('orders/<int:pk>/', OrderDetailAPI.as_view(), name='order-detail-api'),
]