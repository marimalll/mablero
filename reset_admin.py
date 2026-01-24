# reset_admin.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mablero1.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Удаляем старого админа
User.objects.filter(username='admin').delete()

# Создаём нового
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'  # Тот же пароль что в build.sh
)

print("✅ Admin reset successfully!")
print("   Login: admin")
print("   Password: admin123")
print("   URL: /admin/")