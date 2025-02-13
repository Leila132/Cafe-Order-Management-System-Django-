from django.shortcuts import render
from django.db.models import Sum
from orders.models import Order
from django.http import HttpRequest, HttpResponse

def total_paid():
    paid_orders = Order.objects.filter(status='paid')
    total_paid = paid_orders.aggregate(total_sum=Sum('total_price'))['total_sum'] or 0
    return total_paid

def index(request: HttpRequest) -> HttpResponse:
    total_paid_orders = total_paid()
    return render(request, 'main/index.html', {'total_paid': total_paid_orders})

