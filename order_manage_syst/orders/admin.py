from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке заказов
    list_display = ('id', 'table_number', 'total_price', 'status')

    # Поля, которые будут исключены из формы редактирования
    #exclude = ('total_price',)

    # Или, если хотите отображать поле, но сделать его только для чтения
    readonly_fields = ('total_price',)

