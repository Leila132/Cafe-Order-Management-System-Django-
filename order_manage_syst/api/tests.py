from rest_framework.test import APITestCase
from rest_framework import status
from dishs.models import Dish
from orders.models import Order

class DishListAPITestCase(APITestCase):
    def setUp(self):
        """Создаем тестовые данные"""
        self.dish1 = Dish.objects.create(title="Пицца", price=500, is_available=True)
        self.dish2 = Dish.objects.create(title="Бургер", price=300, is_available=False)

    def test_get_dishes_list(self):
        """Тест получения списка блюд"""
        response = self.client.get('/api/dishs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_dish_success(self):
        """Тест создания нового блюда"""
        data = {"title": "Суши", "price": 700, "is_available": True}
        response = self.client.post('/api/dishs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 3) 

    def test_post_dish_not_success(self):
        """Тест создания нового блюда с ошибочными типами данных"""
        data = {"title": "Суши", "price": 'двести', "is_available": True}
        response = self.client.post('/api/dishs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Dish.objects.count(), 2) 
    
class DishDetailAPITestCase(APITestCase):
    def setUp(self):
        """Создаем тестовое блюдо"""
        self.dish = Dish.objects.create(title="Пицца", price=500, is_available=True)
        self.url = f'/api/dishs/{self.dish.id}/'

    def test_get_dish(self):
        """Тест получения одного блюда"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Пицца")
        self.assertEqual(response.data["price"],'500.00')
        self.assertTrue(response.data["is_available"])

    def test_put_dish(self):
        """Тест полного обновления (PUT)"""
        data = {'title': 'Роллы', 'price': 400, 'is_available': False} 
        response = self.client.put(self.url, data, format='json')
        self.dish.refresh_from_db()       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.dish.title, "Роллы")  # Должно обновиться
        self.assertEqual(self.dish.price, 400)
        self.assertFalse(self.dish.is_available)

    def test_patch_dish(self):
        """Тест частичного обновления (PATCH)"""
        data = {'title': 'Кофе'}
        response = self.client.patch(self.url, data, format='json')
        self.dish.refresh_from_db()       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.dish.title, "Кофе") 


class OrderListAPITestCase(APITestCase):
    def test_create_order(self):
        """Тест создания заказа"""
        data = {"customer_name": "Иван", "status": "pending"}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

class OrderListAPITestCase(APITestCase):
    def setUp(self):
        """Создаем тестовые данные"""
        self.dish1 = Dish.objects.create(title="Пицца", price=500, is_available=True)
        self.dish2 = Dish.objects.create(title="Бургер", price=300, is_available=True)
        data = {'table_number': 1, 'items': [self.dish1.id], 'status': 'pending'}
        response = self.client.post('/api/orders/', data, format='json')

    def test_get_orders_list(self):
        """Тест получения списка заказов"""
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_post_dish_success(self):
        """Тест создания нового заказа"""
        data = {'table_number': 2, 'items': [self.dish1.id, self.dish2.id], 'status': 'paid'}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 2) 

    def test_post_dish_not_success(self):
        """Тест создания нового блюда с ошибочными типами данных"""
        data = {'table_number': [2], 'items': [self.dish1.id, self.dish2.id], 'status': 'paid'}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Dish.objects.count(), 2) 
        data = {'table_number': 2, 'items': 'error', 'status': 'paid'}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Dish.objects.count(), 2) 
        data = {'table_number': 2, 'items': [self.dish1.id, self.dish2.id], 'status': 'new'}
        response = self.client.post('/api/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Dish.objects.count(), 2) 

class OrderDetailAPITestCase(APITestCase):
    def setUp(self):
        """Создаем тестовые данные"""
        self.dish1 = Dish.objects.create(title="Пицца", price=500, is_available=True)
        self.dish2 = Dish.objects.create(title="Бургер", price=300, is_available=True)
        data = {'table_number': 1, 'items': [self.dish1.id], 'status': 'pending'}
        response = self.client.post('/api/orders/', data, format='json')
        self.order_id = response.data['id']
        self.url = f'/api/orders/{response.data["id"]}/'
        

    def test_get_order(self):
        """Тест получения одного заказа"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['table_number'], 1)
        self.assertEqual(response.data[ 'items'],  [self.dish1.id])
        self.assertTrue(response.data['status'], 'pending')

    def test_put_order(self):
        """Тест полного обновления (PUT)"""
        data =data = {'table_number': 2, 'items': [self.dish2.id], 'status': 'paid'}
        response = self.client.put(self.url, data, format='json')
        order = Order.objects.get(id=self.order_id)   
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(order.table_number, 2)
        self.assertEqual(list(order.items.values_list('id', flat=True)), [self.dish2.id])
        self.assertEqual(order.status, "paid")

    def test_patch_order(self):
        """Тест частичного обновления (PATCH)"""
        data = {'table_number': 3}
        response = self.client.patch(self.url, data, format='json')
        order = Order.objects.get(id=self.order_id)    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(order.table_number, 3) 