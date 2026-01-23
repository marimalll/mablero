from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
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


from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserRegistrationForm(UserCreationForm):
    # Поле для согласия с условиями
    agree_to_terms = forms.BooleanField(
        required=False,  # Важно: False, проверяем в clean
        label='',
        widget=forms.CheckboxInput(attrs={
            'class': 'terms-checkbox',
            'id': 'id_agree_to_terms'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agree_to_terms'].label = 'Я согласен с условиями использования'

    def clean_agree_to_terms(self):
        agreed = self.cleaned_data.get('agree_to_terms')
        if not agreed:
            raise forms.ValidationError(
                '❌ Вы должны согласиться с условиями использования для регистрации',
                code='terms_not_accepted'
            )
        return agreed

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['image',
            'first_name', 'last_name', 'username', 'email']
        image = forms.ImageField(required=False)
        first_name = forms.CharField()
        last_name = forms.CharField()
        username = forms.CharField()
        email = forms.EmailField()