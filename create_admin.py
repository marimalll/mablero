# create_admin.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mablero1.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Удаляем всех существующих админов
User.objects.filter(username='admin').delete()

# Создаём нового с ПРОСТЫМ паролем
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin'  # ПРОСТОЙ ПАРОЛЬ
)

print("✅ Superuser created: username='admin', password='admin'")