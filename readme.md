# Серверная часть приложения базы данных в архитектуре клиент-сервер

## Запуск миграций

```bash
alembic upgrade head
```

## Запуск сервера

```bash
uvicorn main:app [--port PORT] [--host HOST]
```

> `/docs` - OpenAPI-документация запущенного сервера, `/admin` - панель администратора запущенного сервера
