#!/bin/sh

# Применяем миграции
python manage.py migrate

# Создаём админа
python manage.py create_admin

# Создаём неактивного пользователя
python manage.py create_inactive_user

# Загружаем тестовые данные
python manage.py load_test_data

# Запускаем Django-сервер
python manage.py runserver 0.0.0.0:8000
