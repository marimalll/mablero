from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm


# Create your views here.
def login (request):
    if request.method == 'POST':
        form = UserLoginForm(data= request.POST)
        if form.is_valid():
            # аутентификация - проверяем данные
            username = request.POST['username']
            password = request.POST['password']
            # проверка на совпадение данных, введенныз пользователем с его данными в бд
            user = auth.authenticate(username=username, password=password)
            # только если аутентификация прошла успешно - авторизация пользователя
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {'title': 'mablero - Авторизация',
               'form': form}
    return render(request, 'users/login.html', context)
def logout (request):
    ...
def profile(request):
    context = {'title': 'mablero - Кабинет'}
    return render(request, 'users/profile.html', context)

def registration(request):
    context = {'title': 'mablero - Регистрация'}
    return render(request, 'users/registration.html', context)