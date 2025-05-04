# API для Yatube

**Yatube API** - RESTful API для проекта Yatube, соцсети, которая позволяет пользователям создавать посты, комментировать их, подписываться на других пользователей и взаимодействовать с группами.

## Описание проекта

**Yatube API** предоставляет возможность управлять контентом через HTTP-запросы, что делает его удобным для интеграции с мобильными приложениями, веб-сайтами и другими сервисами.

## Локальный запуск

- Клонируем репозиторий и переходим в папку с проектом:
```bash
mkdir yandex && cd yandex
git clone https://github.com/ErikBjornson/api_final_yatube.git
cd api_final_yatube
```

- Создаём виртуальное окружение и активируем его:
```bash
python -m venv .venv
cd .venv/Scripts/activate
```

- Устанавливаем все зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Выполняем миграции проекта:
```bash
cd yatube_api
python manage.py makemigrations
python manage.py migrate
```

- Запускаем сервер:
```bash
python manage.py runserver
```

## Примеры доступных запросов к API

### Просмотр списка постов

- Запрос
```bash
GET /api/v1/posts/
```

- Ответ
```bash
{
  "count": 100,
  "next": "http://api.example.org/accounts/?offset=150&limit=100",
  "previous": "http://api.example.org/accounts/?offset=150&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2025-05-04T12:49:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Просмотр комментариев к посту

- Запрос
```bash
GET /api/v1/posts/{post_id}/comments/
```

- Ответ
```bash
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2025-05-04T12:49:29.648Z",
    "post": 0
  }
]
```

### Подписка на пользователя - автора поста

- Запрос
```bash
POST /api/v1/follow/
```

- Тело запроса
```bash
{
  "following": "username"
}
```

- Ответ
```bash
{
  "user": "string",
  "following": "string"
}
```

### Создание нового поста

- Запрос
```bash
POST /api/v1/posts/
```

- Тела запроса
```bash
{
  "text": "Текст нового поста",
  "image": "string",
  "group": 1
}
```

- Ответ
```bash
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2025-05-04T12:49:29.648Z",
  "image": "string",
  "group": 1
}
```

## Документация к API

Более подробная документация по проекту доступна по адресу http://127.0.0.1:8000/redoc/ после запуска сервера.
