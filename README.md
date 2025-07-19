# Electronics Retail Chain

**Система учёта цепочек поставок электроники: от завода до ИП**

## 📦 Описание

Django-приложение с REST API для управления иерархией поставщиков:
- заводы, дистрибьюторы, магазины, ИП
- фильтрация по стране и городу
- учёт задолженности
- доступ к API только для активных пользователей

---

## 🚀 Технологии

- Python 3.11
- Django 3+
- Django REST Framework
- PostgreSQL
- Docker + Docker Compose
- drf-spectacular (OpenAPI)

---

## ⚙️ Установка

```bash
git clone https://github.com/maxmaleev1/electronics_retail_chain.git
cd electronics_retail_chain
poetry install
```

Создай файл `.env` на основе `.env.example`

---

## 🐳 Запуск в Docker

Перед первым запуском необходимо собрать образы:

```bash
docker-compose build
```

Затем запусти контейнеры:

```bash
docker-compose up -d
```

После запуска:
- Приложение: http://localhost:8000
- Документация: http://localhost:8000/api/schema/swagger-ui/

---

## 📁 Примеры API

- `GET /api/linkchain/` — список звеньев
- `POST /api/linkchain/` — создать звено
- `GET /api/linkchain/?country=Россия` — фильтрация по стране

---

## 👨‍💻 Автор

Максим Малеев  
[https://github.com/maxmaleev1](https://github.com/maxmaleev1)

---

## 📄 Лицензия

Проект распространяется под лицензией MIT.
