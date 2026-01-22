from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


# форма, связанная с моделью бд,  для проверки уже зарегистрированных пользователей
class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    # username = forms.CharField(lable="Имя пользователя",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   "class":"form-group",
    #                                   "placeholder":"Введите ваше имя пользователя"}))
    # password = forms.CharField(
    #     lable="Пароль",widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       "class":"form-group",
    #                                       "placeholder":"Введите ваш пароль"}),
    # )
    class Meta:
        model = User
        fields = ['username', 'password']