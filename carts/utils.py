from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key)
    return carts.order_by('id')