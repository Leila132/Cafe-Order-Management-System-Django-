from django.test import TestCase, Client
from .views import total_paid
from orders.models import Order
from dishs.models import Dish
from django.urls import reverse

class GetPaidOrdersSumTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('add_order')
        Dish.objects.create(id=3, title="Суп", price=50.00, is_available=True)
        Dish.objects.create(id=6, title="Каша", price=20.00, is_available=True)

    def test_add_dish_post_valid(self):

        data = {
            'table_number': 1,
            'items': [3, 6],
            'status': 'paid'
        }
        response = self.client.post(self.url, data)
        data = {
            'table_number': 1,
            'items': [3],
            'status': 'paid'
        }
        response = self.client.post(self.url, data)
        data = {
            'table_number': 1,
            'items': [3],
            'status': 'ready'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(total_paid(), 120.00)