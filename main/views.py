from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': "mablero - главная",
        'title1': "Мебель для вашего дома",
        'title2': "Всё, что нужно для уюта",
        'text': "Представьте место, где каждая вещь на своем месте, а мягкий диван словно ждет вас. \n Наша мебель создана не для галочки, а для того, чтобы наполнить ваш дом теплом и уютом."
    }
    return render(request, 'main/index.html', context)

def contacts(request):
    context = {
        'title': "mablero - контакты",
        'title1': "Наши контакты"
    }
    return render(request, 'main/contacts.html', context)

def cart(request):
    context = {
        'title': "mablero - корзина",
        'title1': "пока что пусто"
    }
    return render(request, 'main/cart.html', context)

# позднее тоже переместить
def favourites(request):
    context = {
        'title': "mablero - избранное",
        'title1': "Вы пока не добавили товары в избранное",
        'text': "Найдите подходящую мебель в каталоге и добавляйте понравившиеся товары в избранное, чтобы не потерять их"

    }
    return render(request, 'main/favourites.html', context)
