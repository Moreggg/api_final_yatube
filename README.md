## Описание:

Финальный проект с API для сервиса Yatube

Yatube — это платформа для блогов. Данный сервис предоставляет возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

## Используемый стек

- Django
- Django Rest Framework
- Djoser
- Simple JWT

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Moreggg/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```

```
source env/bin/activate
```


Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Документация к проекту находится по адресу:

```
/redoc/
```

## Примеры запросов:
Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.
```
GET /api/v1/posts/
```
Пример ответа:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
```
POST /api/v1/posts/
```
Пример запроса:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Получение списка доступных сообществ.
```
GET /api/v1/groups/
```
Пример ответа:
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
Возможен поиск по подпискам по параметру search
```
GET /api/v1/follow/
```
Пример ответа:
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
POST /api/v1/follow/
```
Пример запроса:
```
{
  "following": "string"
}
```

Пример ответа:
```
{
  "user": "string",
  "following": "string"
}
```

## Команда проекта

Евгений Чередниченко 
https://github.com/Moreggg
