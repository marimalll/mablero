from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

from users.forms import UserLoginForm, UserRegistrationForm


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
    auth.logout(request)
    return redirect(reverse('main:index'))
def profile(request):
    context = {'title': 'mablero - Кабинет'}
    return render(request, 'users/profile.html', context)

@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'mablero - Регистрация',
               'form': form}
    return render(request, 'users/registration.html', context)