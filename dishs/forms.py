from .models import Dish
from django.forms import ModelForm, TextInput, CheckboxInput

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['title', 'price', 'is_available']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название блюда'
            }), 
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена блюда'
            }),
            "is_available": CheckboxInput(attrs={
                'class': 'form-check-input', 
            }),
        } 