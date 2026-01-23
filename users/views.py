from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth, messages
from django.views.decorators.csrf import csrf_protect

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm



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
                messages.success(request, f"{username}, Вы вошли в аккаунт")
                if request.POST.get('next', None):
                    return redirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {'title': 'mablero - Авторизация',
               'form': form}
    return render(request, 'users/login.html', context)
@login_required
def logout (request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {'title': 'mablero - Кабинет', 'form': form}
    return render(request, 'users/profile.html', context)

@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрировались")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'mablero - Регистрация',
               'form': form}
    return render(request, 'users/registration.html', context)