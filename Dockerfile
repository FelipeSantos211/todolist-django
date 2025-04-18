FROM python:3.13.3-alpine

# Instalar dependências do sistema (compiladores, libpq, etc.)
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    musl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    python3-dev \
    gcc \
    cargo \
    bash

WORKDIR /app

COPY requirements.txt /app/

# Instala as dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Comando de execução
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

