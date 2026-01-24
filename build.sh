#!/usr/bin/env bash
echo "=== Building Django project ==="

# 1. Установка зависимостей
pip install -r requirements.txt

# 2. Сборка статики
python manage.py collectstatic --noinput

# 3. Миграции
python manage.py migrate --noinput

# 4. Загрузка фикстур (если есть)
echo "=== Loading fixtures ==="
if [ -f "fixtures/goods/categories.json" ]; then
    python manage.py loaddata fixtures/goods/categories.json
    echo "✅ Categories loaded"
fi

if [ -f "fixtures/goods/products.json" ]; then
    python manage.py loaddata fixtures/goods/products.json
    echo "✅ Products loaded"
fi

# 5. СОЗДАНИЕ АДМИНА (самое важное!)
echo "=== Creating/resetting admin ==="
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'
password = 'admin123'  # ПРОСТОЙ ПАРОЛЬ
email = 'admin@example.com'

# Удаляем старого админа если есть
User.objects.filter(username=username).delete()

# Создаём нового
try:
    user = User.objects.create_superuser(username, email, password)
    print(f'✅ Superuser created: {username} / {password}')
except Exception as e:
    print(f'❌ Error creating admin: {e}')
"

# 6. Проверка данных
echo "=== Verifying data ==="
python manage.py shell -c "
from goods.models import Categories, Products
from django.contrib.auth import get_user_model
User = get_user_model()

print('--- Database Status ---')
print(f'👑 Admin users: {User.objects.filter(is_superuser=True).count()}')
print(f'📊 Categories: {Categories.objects.count()}')
print(f'📦 Products: {Products.objects.count()}')

if Categories.objects.count() > 0:
    print('Sample categories:')
    for cat in Categories.objects.all()[:3]:
        print(f'  - {cat.name} ({cat.slug})')
"

echo "=== Build completed successfully! ==="