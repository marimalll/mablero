from django.shortcuts import render
from goods.models import Categories, Products

def catalog(request):

    goods = Products.objects.all()
    categories = Categories.objects.all()
    context = {'categories': categories,
               "goods": goods,}
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    contexct = {
        'product': product,
    }
    return render(request, 'goods/product.html', context=contexct)
