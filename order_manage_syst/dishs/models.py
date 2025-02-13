from django.db import models


class Dish(models.Model):
    title = models.CharField('Название', max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True, verbose_name='Доступность') 
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def get_absolute_url(self):
        	return f'/dishs/{self.id}'