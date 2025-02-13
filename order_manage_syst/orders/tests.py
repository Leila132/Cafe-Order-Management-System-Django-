from django.test import TestCase, Client
from .models import Order
from dishs.models import Dish
from django.urls import reverse

class AddOrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('add_order')
        Dish.objects.create(id=3, title="Суп", price=50.00, is_available=True)
        Dish.objects.create(id=6, title="Каша", price=20.00, is_available=True)

    def test_add_dish_post_valid(self):

        data = {
            'table_number': 1,
            'items': [3, 6],
            'status': 'pending'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.first().total_price, 70)