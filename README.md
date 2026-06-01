# Case-task-3

## Django Greeting App

Веб-приложение на Django, позволяющее ввести свое имя и получить персонализированное приветствие.

## Функционал

- Ввод имени через форму
- Сохранение имени в базе данных
- Отображение персонализированного приветствия
- Обработка ошибок (пустое поле)
- Защита от CSRF-атак
- Стилизация интерфейса с использованием CSS

---
## Технологии
- Python 3
- Django
- HTML5
- CSS3

---
## Структура проекта
- manage.py
- config/
  - settings.py
  - urls.py
- greetings/
  - models.py
  - views.py
  - forms.py
  - urls.py
- templates/
  - greetings/
    - home.html
- static/
  - style.css

 ---
 ## Установка и запуск

 1. Клонирование репозитория: git clone https://github.com/Storlard/Case-task-3.git
 2. Создание виртуального пространства из папки проекта: python -m venv venv
 3. Активация виртуального пронстранства: venv\Scripts\activate
 4. Применение миграции: pyton manage.py migrate
 5. Запуск сервера: python manage.py runserver
 6. Открытие приложения в браузере: http://127.0.0.1:8000/

---
## Безопасность
Используется встроенная защита Django от CSRF: {% csrf_token %}
