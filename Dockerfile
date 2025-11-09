FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Dependencias para psycopg2
RUN apt-get update && apt-get install -y \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install poetry

# Copiar dependencias
COPY pyproject.toml poetry.lock ./

# Instalar sin venv
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# Copiar código
COPY . .

# Recolectar archivos estáticos
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Gunicorn para producción
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]