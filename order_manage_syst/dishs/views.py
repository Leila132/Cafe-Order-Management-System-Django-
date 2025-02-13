from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Dish
from .forms import DishForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from typing import Optional

def dishs_home(request: HttpRequest) -> HttpResponse:
    dishs = Dish.objects.all().order_by('-is_available', 'title')
    return render(request, 'dishs/dishs.html', {'dishs': dishs})

def add_dish(request: HttpRequest) -> HttpResponse:
    form_errors: Optional[dict] = None
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dishs')
        else:
            form_errors = form.errors 
    else:
        form = DishForm()

    data = {
        'form': form,
        'form_errors': form_errors,
    }
    return render(request, 'dishs/add_dish.html', data)

class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'dishs/add_dish.html'
    form_class = DishForm
    success_url = reverse_lazy('dishs')