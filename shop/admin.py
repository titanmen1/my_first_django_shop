from django.contrib import admin
from .models import Product, Category, Brand, CartItem, Cart, Order
# Register your models here.


def make_payed(modeladmin, request, queryset):  # новое действие с заказами(изменение статуса как оплачен)
    queryset.update(status='Оплачен')
make_payed.short_description = 'Пометить как оплаченные'


def make_in_process(modeladmin, request, queryset):  # новое действие с заказами(изменение статуса как оплачен)
    queryset.update(status='Выполняется')
make_in_process.short_description = 'Пометить как выполняется'



class OrderAdmin(admin.ModelAdmin):  # добавление фильтров и активностей в заказы
    list_filter = ['status']
    actions = [make_payed, make_in_process]

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
