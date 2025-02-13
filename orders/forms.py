from .models import Order, Dish
from django.forms import ModelForm, NumberInput, SelectMultiple, Select

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']
        widgets = {
            'table_number': NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 99,
            }),
            'items': SelectMultiple(attrs={
                'class': 'form-control',
            }),
            'status': Select(attrs={
                'class': 'form-control',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтруем блюда, чтобы отображались только доступные
        self.fields['items'].queryset = Dish.objects.filter(is_available=True).order_by('title')