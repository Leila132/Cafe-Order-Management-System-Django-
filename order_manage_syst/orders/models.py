from django.db import models
from dishs.models import Dish
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from decimal import Decimal

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    id = models.AutoField(primary_key=True)

    table_number = models.IntegerField(
        'Номер стола',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99)
        ]
    )

    items = models.ManyToManyField(
        Dish,
        related_name='orders',
        verbose_name='Блюда'
    )

    total_price = models.DecimalField(
        'Общая стоимость',
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        'Статус',
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f'Заказ #{self.id} (Стол {self.table_number})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def calculate_total_price(self) -> Decimal:
        """
        Вычисляет общую стоимость заказа на основе выбранных блюд.
        """
        return sum((item.price for item in self.items.all()), Decimal(0))

# Сигнал для пересчета общей стоимости при изменении items
@receiver(m2m_changed, sender=Order.items.through)
def update_total_price(sender, instance, action, **kwargs):
    """
    Сигнал для пересчета общей стоимости заказа при изменении блюд.
    """
    # Пересчитываем общую стоимость только при добавлении или удалении связи
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.total_price = instance.calculate_total_price()
        instance.save()