# Django TODO list

Невеликий навчальний проєкт на **Django** — сайт для управління завданнями (*todo list*).

## 🔧 Встановлення та запуск
```bash
git clone https://github.com/Andriy125/django-todo.git
cd django-todo
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Відкрий у браузері:
👉 http://127.0.0.1:8000/

## 📋 Функціонал

### Task

* текст завдання

* дата створення

* опціональний дедлайн

* статус (done / not done)

* теги (many-to-many)

### Tag

* назва (унікальна)

## 🖼️ Інтерфейс

* Головна (/) — список завдань, кнопки Add / Update / Delete / Complete / Undo

* Сторінка тегів (/tags/) — список тегів, кнопки Add / Update / Delete

* Sidebar з навігацією (Home, Tags) на всіх сторінках

## 🚀 Технології

* Python 3.13.5

* Django 5.2

* Bootstrap 5 (оформлення)