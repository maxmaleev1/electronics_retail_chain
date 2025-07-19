# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только pyproject.toml и poetry.lock для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Копируем entrypoint
COPY entrypoint.sh /app/entrypoint.sh

# Делаем его исполняемым
RUN chmod +x /app/entrypoint.sh

# Устанавливаем точку входа
ENTRYPOINT ["/app/entrypoint.sh"]
