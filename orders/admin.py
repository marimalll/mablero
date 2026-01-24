from django.contrib import admin

# Register your models here.
from orders.models import Order, OrderItem


admin.site.register(OrderItem)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'name', 'quantity', 'price')
    search_fields = ('name', 'product', 'order')

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = 'product', 'name', 'price', 'quantity'
    extra = 0
    search_fields = ('name', 'product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    )
    readonly_fields = ('created_timestamp',)
    inlines = (OrderItemTabulareAdmin,)

class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    list_display = (
        'id',
        'user',
        'requires_delivery',
        'status',
        'payment_on_get',
        'is_paid',
        'created_timestamp',
    )
    fields = ('requires_delivery', 'status', 'payment_on_get', 'is_paid', 'created_timestamp')
    search_fields = ('requires_delivery', 'payment_on_get', 'is_paid', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0