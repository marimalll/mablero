from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order
from django.db import transaction
from django.shortcuts import render
from django.contrib import auth, messages

from orders.models import OrderItem


# Create your views here.
@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    if cart_items.exists():
                        # create order
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery = form.cleaned_data['requires_delivery'],
                            delivery_address = form.cleaned_data['delivery_address'],
                            payment_on_get = form.cleaned_data['payment_on_get'],
                        )
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.price
                            quantity = cart_item.product.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f"Недостаточное количество товаров {name} на складе\ В наличии - {product.quantity}")

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                quantity=quantity,
                                name=name,
                                price=price,
                            )
                            product.quantity -= quantity
                            product.save()

                        cart_items.delete()

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)
    context = {
        'title': 'Create Order',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context)
