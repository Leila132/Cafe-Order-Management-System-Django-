from rest_framework import serializers
from dishs.models import Dish
from orders.models import Order
from typing import Type, List

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model: Type[Dish] = Dish
        fields: List[str] = ['id', 'title', 'price', 'is_available']

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=Dish.objects.all(), many=True)
    class Meta:
        model: Type[Order] = Order
        fields: List[str] = ['id', 'table_number', 'items', 'total_price', 'status']