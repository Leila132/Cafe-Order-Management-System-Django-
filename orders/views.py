from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse

def orders_home(request:HttpRequest) -> HttpResponse:
    table_number = request.GET.get('table_number')
    status = request.GET.get('status')
    orders = Order.objects.all().order_by('-status')

    if table_number:
        orders = orders.filter(table_number=table_number)
    
    if status:
        orders = orders.filter(status=status)

    return render(request, 'orders/orders.html', {'orders': orders})

def add_order(request:HttpRequest) -> HttpResponse:
    form_errors = None 

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
        else:
            form_errors = form.errors 
    else:
        form = OrderForm()

    data = {
        'form': form,
        'form_errors': form_errors,
    }
    return render(request, 'orders/add_order.html', data)

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'orders/add_order.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders')

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/orders'
    template_name = 'orders/orders_delete.html'