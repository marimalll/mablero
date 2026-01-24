import re

from django import forms

class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "+7 (999) 123-45-67",
        }),
        help_text="Формат: +7 XXX XXX-XX-XX"
    )
    requires_delivery = forms.ChoiceField(choices=[
            ("0", False),
            ("1", True),
        ],
        initial=0,)

    delivery_address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'г. Москва, ул. Примерная, д. 1, кв. 1'})
    )
    payment_on_get = forms.ChoiceField(choices=[
            ("0", False),
            ("1", True),
        ],
        initial=0,)

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number', '')

        if not phone:
            raise forms.ValidationError("Введите номер телефона")

        # Удаляем все нецифровые символы, кроме плюса в начале
        cleaned = re.sub(r'[^\d+]', '', phone)

        # Обработка различных форматов ввода
        if cleaned.startswith('+7'):
            # Формат: +79991234567
            digits = cleaned[2:]  # удаляем +7
        elif cleaned.startswith('7'):
            # Формат: 79991234567
            digits = cleaned[1:]  # удаляем первую 7
        elif cleaned.startswith('8'):
            # Формат: 89991234567 (российский с 8)
            digits = cleaned[1:]  # удаляем первую 8
        elif cleaned.startswith('9') and len(cleaned) == 10:
            # Формат: 9991234567 (только 10 цифр без кода страны)
            digits = cleaned
        elif cleaned.startswith('+') and not cleaned.startswith('+7'):
            # Неправильный международный код
            raise forms.ValidationError(
                "Используйте российский формат номера (+7)"
            )
        else:
            # Пробуем понять формат
            if len(cleaned) == 10 and cleaned[0] in '345689':
                digits = cleaned
            else:
                raise forms.ValidationError(
                    "Неверный формат номера. Пример: +7 (999) 123-45-67"
                )

        # Проверка длины (10 цифр после +7)
        if len(digits) != 10:
            raise forms.ValidationError(
                f"Номер должен содержать 10 цифр после +7. Вы ввели {len(digits)} цифр"
            )

        # Проверка, что первая цифра после +7 - 9,8,5,4,3 (валидные коды РФ)
        if digits[0] not in '345689':
            raise forms.ValidationError(
                "Неверный код оператора"
            )

        # Форматируем номер в единый формат
        formatted_phone = f"+7{digits}"

        # Дополнительная проверка с регулярным выражением
        if not re.match(r'^\+7[345689]\d{9}$', formatted_phone):
            raise forms.ValidationError(
                "Неверный формат номера телефона"
            )

        return formatted_phone

    def clean_delivery_address(self):
        requires_delivery = self.cleaned_data.get('requires_delivery')
        address = self.cleaned_data.get('delivery_address', '').strip()

        if requires_delivery == "1":
            if not address:
                raise forms.ValidationError("Укажите адрес доставки")

            # Проверка минимальной длины
            if len(address) < 15:
                raise forms.ValidationError("Адрес должен содержать не менее 15 символов")

            # Проверка на наличие номера дома (простая проверка)
            if not re.search(r'\d', address):
                raise forms.ValidationError("Укажите номер дома в адресе")

            # Проверка на наличие улицы/проспекта
            street_patterns = r'(ул\.|улица|проспект|пр\.|бульвар|б-р|переулок|пер\.|шоссе)'
            if not re.search(street_patterns, address, re.IGNORECASE):
                raise forms.ValidationError("Укажите улицу/проспект в адресе")

        return address
    # last_name = forms.CharField(max_length=10, required=True)
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введите ваше имя',
    #         }
    #     )
    # )
    # last_name = forms.CharField(widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введите вашу фамилию',
    #         }
    #     ))
    #
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введите номер телефона',
    #         }
    #     ))
    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0,
    # )
    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'delivery-address',
    #             'rows': 2,
    #             'placeholder': 'Введите адрес доставки',
    #         }
    #     ))
    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0,
    # )

