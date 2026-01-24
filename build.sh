#!/usr/bin/env bash
echo "=== Building Django project ==="
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
echo "=== Build completed ==="
