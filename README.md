# Currency Quotes
## Запуск
Приложение состоит из двух частей: 
- бэкенд на python - FastApi
- фронтенд на React
- упаковка Docker

Для запуска приложения, после клонирования репозитория, зайти в терминале в корневую папку и запустить команду
```
docker-compose up
```
Docker автоматически поднимет два сервииса, которые будут общатся между собой

`http://localhost:3000/` - фронтенд прилодение

`http://localhost:8000/docs` - API, можно потестить доступные методы (авторизация не требуется)

Чтобы завершить работу контейнера нажмите сочетание клавиш `Ctrl+C`
## Как это работает
Вся логика находится на стороне сервера (FastApi). React приложение только отправляет запросы, принимает ответ и отрисовывает все в браузере.

На стороне сервера реализована система CRUD для данных и нужные методы, эндпоинты для выполнения основныйх задач тестового.

Интерфейс интуитивно понятен и вопросов о работе вызывать не должен. Если будут вопросы по реализации и работе сервисов готов связвтся и обсудить.

## P.S.
- кнопки экспорта появятся только после генерации таблицы