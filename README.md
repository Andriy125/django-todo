# Django TODO List

A small practice project built with Django — a site to manage tasks.

## Features
- Tasks with: content, created datetime, optional deadline, done flag, and tags (many-to-many)
- Tags with unique name
- Home page: ordered tasks (not done first, newest first), show all fields, buttons: Add / Update / Delete / Complete / Undo
- Tag list page: table of tags with Add / Update / Delete
- Sidebar navigation visible on all pages

## Tech
- Python 3.13
- Django 5.2
- Bootstrap 5

## Setup
```bash
git clone https://github.com/Andriy125/django-todo.git
cd django-todo
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
