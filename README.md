# Асинхронный парсер на Scrapy

[![async-parcer workflow](https://github.com/alex-zharinov/async_parcer/actions/workflows/main.yml/badge.svg)](https://github.com/alex-zharinov/async_parcer/actions/workflows/main.yml)

## Парсинг документов PEP
> Парсер собирает данные обо всех PEP документах, сравнивает статусы и записывает их в два файла,
также реализованы сбор информации о статусе версий, скачивание архива с документацией и сбор ссылок о новостях в Python.

## Технологии проекта
- Python — высокоуровневый язык программирования;
- Scrapy — это высокоуровневый Python-фреймворк для парсинга данных с веб-сайтов, построенный на базе асинхронной библиотеки Twisted;
- SQLAlchemy — это Python-библиотека, которая позволяет работать с реляционными базами данных с помощью ORM.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/alex-zharinov/async_parcer.git
```
```
cd async_parcer
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Запустить парсер:
```
scrapy crawl quotes
```

### Вывод парсера:
Парсер должен выводит собранную информацию в два файла .csv:
1. В первый файл записывает список всех PEP: номер, название и статус.
2. Во второй файл записывает сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» стоит Total, а в колонке «Количество» — общее количество всех документов.

## Автор
[Жаринов Алексей](https://github.com/alex-zharinov)
