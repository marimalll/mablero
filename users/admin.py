from django.contrib import admin

# Register your models here.

from users.models import User

from carts.admin import CartTabAdmin

from orders.admin import OrderTabulareAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'password']

    inlines = [CartTabAdmin, OrderTabulareAdmin]