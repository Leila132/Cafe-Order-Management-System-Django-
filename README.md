# Cafe-Order-Management-System-Django-

Веб-приложение, разработанное на Django с использованием Django REST Framework для управления заказами в кафе. Приложение позволяет добавлять, удалять, искать, изменять и отображать заказы. Содержит API для взаимодействия с приложением, протестированы оснеовные функции с помощью unittest и расширений Django TestCase, Django REST Framework APITestCase.

## Требования

Python 3.9

## Установка

1. Клонируйте репозиторий:

`git clone https://github.com/Leila132/Cafe-Order-Management-System-Django-.git`

2. Перейдите в директорию проекта:

`cd Cafe-Order-Management-System-Django-`

3. Установите зависимости:

`pip install -r requirements.txt`

## Запуск

Чтобы запустить проект, выполните:

`python manage.py runserver`

## Использование

Приложение позволяет формировать заказы, которые включают в себя следующие поля: номер стола, блюда, статус (определено только 3 статуса: "в ожидании", "готово", "оплачено"). В свою очередь блюда содержат информацию: название, цена, доступность (не реализована возможность удаления блюд, чтобы не удалять заказы, которые включали в себя удаленные блюда, поэтому можно "выключить" доступность блюда, тогда прежние заказы с этими блюдами останутся, а новые заказы с этим блюдом нельзя будет оформить)
Интерфейс приложения выглядит следющим образом. На вклаке "Блюда" можно посмотреть добавленные блюда и их доступность.

![](images/dishs.png)


