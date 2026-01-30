from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'name', 'price', 'quantity']
    readonly_fields = ['name', 'price']  # Только просмотр
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_info', 'requires_delivery', 'status', 'payment_on_get', 'is_paid',
                    'created_timestamp', 'total_price']
    list_filter = ['status', 'is_paid', 'created_timestamp']
    search_fields = ['user__username', 'phone_number']
    readonly_fields = ['created_timestamp']
    inlines = [OrderItemInline]
    def get_user_info(self, obj):
        try:
            if obj.user:
                return str(obj.user.username)
            return "Гость"
        except: return "Ошибка"
    get_user_info.short_description = 'Пользователь'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'name', 'quantity', 'price', 'products_price']
    list_filter = ['order__status']
    search_fields = ['name', 'product__name']


    def products_price(self, obj):
        return obj.products_price()
    products_price.short_description = 'Общая стоимость'
