from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from dishs.models import Dish
from orders.models import Order
from .serializers import DishSerializer, OrderSerializer
from rest_framework.request import Request
from rest_framework.response import Response

# API для списка блюд (GET, POST)
class DishListAPI(APIView):
    def get(self, request: Request) -> Response:
        dishs = Dish.objects.all().order_by('-is_available', 'title')
        serializer = DishSerializer(dishs, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для работы с одним блюдом (GET, PUT, PATCH, DELETE)
class DishDetailAPI(APIView):
    def get(self, request, pk) -> Response:
        dish = get_object_or_404(Dish, pk=pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data)

    def put(self, request: Request, pk:int) -> Response:
        dish = get_object_or_404(Dish, pk=pk)
        serializer = DishSerializer(dish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk:int) -> Response:
        dish = get_object_or_404(Dish, pk=pk)
        serializer = DishSerializer(dish, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# API для списка заказов (GET, POST)
class OrderListAPI(APIView):
    def get(self, request: Request) -> Response:
        orders = Order.objects.all().order_by('-status')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# API для работы с одним заказом (GET, PUT, PATCH, DELETE)
class OrderDetailAPI(APIView):
    def get(self, request: Request, pk:int) -> Response:
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request: Request, pk:int) -> Response:
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk:int) -> Response:
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk:int) -> Response:
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response({"message": "Заказ удален"}, status=status.HTTP_204_NO_CONTENT)