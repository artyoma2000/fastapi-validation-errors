# 🚀 Учебный проект по валидации данных и обработке ошибок в FastAPI

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-brightgreen)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/downloads/release/python-390/)
[![License](https://img.shields.io/badge/License-MIT-yellowgreen)](LICENSE)

## 🎯 Особенности

- **Валидация данных**: Проверка входных данных с помощью Pydantic.
- **Обработка ошибок**: Персонализированная обработка ошибок для повышения информативности.
- **FastAPI**: Современный и быстрый фреймворк для создания API.

## 🚀 Как начать

### Требования

- Python 3.9+
- Менеджер пакетов `pip`

### Установка

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/artyoma2000/fastapi-validation-errors.git
   cd fastapi-validation-errors
   ```

2. **Создание и активация виртуального окружения**:
   ```bash
   python -m venv env
   source env/bin/activate  # Для Windows используйте `env\Scripts\activate`
   ```

3. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

### Запуск проекта

1. **Запуск сервера FastAPI**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Доступ к документации API**:
   - Откройте [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) для Swagger UI.
   - Или [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) для ReDoc.

## 🛠️ Использование

### Пример запроса

1. **Создание пользователя**:
   ```http
   POST /user/
   Content-Type: application/json

   {
     "username": "john_doe",
     "age": 25,
     "email": "john@example.com",
     "password": "super_secret123",
     "phone": "1234567890"
   }
   ```

2. **Получение ответа об ошибке (неверный возраст)**:
   ```http
   POST /user/
   Content-Type: application/json

   {
     "username": "john_doe",
     "age": 17,  # Возраст меньше 18
     "email": "john@example.com",
     "password": "super_secret123",
     "phone": "1234567890"
   }

   Ответ:
   {
     "detail": "Ошибка проверки данных",
     "errors": ["body -> age: Input should be greater than 18"]
   }
   ```

### Тестирование

1. **Запуск тестов**:
   ```bash
   pytest test_main.py
   ```

   Тесты проверяют корректность работы обработки ошибок и валидации данных.

## 📄 API Эндпоинты

- **`POST /user/`**: Создает нового пользователя при успешной валидации данных.

## 🔧 Структура проекта

```
fastapi-validation-errors/
│
├── main.py             # Основной файл приложения FastAPI
├── test_main.py        # Тесты для проверки валидации и обработки ошибок
├── requirements.txt    # Файл зависимостей
└── README.md           # Документация проекта
```

## 🧩 Расширение проекта

- **Добавление новых моделей данных**: Расширьте или добавьте новые Pydantic модели для различных сценариев валидации.
- **Добавление новых эндпоинтов**: Реализуйте дополнительные эндпоинты для работы с пользователями или другими сущностями.
- **Интеграция с базой данных**: Подключите SQLAlchemy или другую ORM для работы с реальными данными.

## 🤝 Участие

Ваш вклад в проект приветствуется! Если у вас есть идеи по улучшению, пожалуйста, создавайте issue или pull request.

- [Документация FastAPI](https://fastapi.tiangolo.com)
- [Документация Pydantic](https://pydantic-docs.helpmanual.io)

