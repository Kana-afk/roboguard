**Название Проекта**: TechTrack Equipment Management System

**Описание**:
TechTrack Equipment Management System — это RESTful API, разработанный для управления и мониторинга технического оборудования. API позволяет пользователям выполнять CRUD операции (создание, чтение, обновление, удаление) над данными оборудования, включая машины, роботы и сенсоры. Система также поддерживает отслеживание операционных данных, таких как температура, скорость и давление, и предоставляет возможность создавать предупреждения для уведомления операторов о важных событиях или состояниях оборудования.

Разработанный с использованием Django и Django REST Framework, этот проект включает в себя мощные функции безопасности, такие как аутентификация на основе токенов, и предоставляет автоматически сгенерированную документацию с помощью DRF-yasg для удобства использования API. TechTrack предназначен для предприятий, стремящихся оптимизировать управление своим техническим парком через автоматизированные цифровые решения, обеспечивая при этом высокую точность и доступность данных.

## Особенности

основные особенности и возможности моего проекта, такие как:
- CRUD операции для оборудования.
- Аутентификация и авторизация с использованием токенов.
- Автоматическая документация API с использованием Swagger.

## Технологии

основные технологии и фреймворки, которые использовались в проекте:
- Django 3.2
- Django REST Framework
- DRF-yasg для Swagger

## Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/Kana-afk/roboguard.git

```
2. Установите зависимости:
```bash
   pip install -r requirements.txt
```
3. Создайте базу данных PostgreSQL и настройте соединение в файле settings.py.
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Your_database',
        'USER': 'Your_username',
        'PASSWORD': 'Your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
4. Выполните миграции:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустите сервер:
```bash
python manage.py runserver
```
## API Endpoints

Ниже приведен список основных API endpoints с описанием их функций:

### Equipment

- `GET /api/equipment/`
  - Получение списка всего оборудования.
  - **Пример запроса**: `GET http://127.0.0.1:8000/api/equipment/`
  - **Требует аутентификации**: Да

- `POST /api/equipment/`
  - Создание новой записи оборудования.
  - **Пример запроса**: `POST http://127.0.0.1:8000/api/equipment/`
  - **Требует аутентификации**: Да
  - **Тело запроса**:
    ```json
    {
      "name": "New Equipment",
      "equipment_type": "machine",
      "model": "Model X1",
      "installation_date": "2023-01-01",
      "status": "active"
    }
    ```

- `PUT /api/equipment/{id}/`
  - Обновление информации о существующем оборудовании.
  - **Пример запроса**: `PUT http://127.0.0.1:8000/api/equipment/1/`
  - **Требует аутентификации**: Да

- `DELETE /api/equipment/{id}/`
  - Удаление записи оборудования.
  - **Пример запроса**: `DELETE http://127.0.0.1:8000/api/equipment/1/`
  - **Требует аутентификации**: Да

### Data

- `GET /api/data/`
  - Получение списка данных, связанных с оборудованием.
  - **Пример запроса**: `GET http://127.0.0.1:8000/api/data/`
  - **Требует аутентификации**: Да

### Alerts

- `GET /api/alerts/`
  - Получение списка всех предупреждений.
  - **Пример запроса**: `GET http://127.0.0.1:8000/api/alerts/`
  - **Требует аутентификации**: Да

Эти endpoints позволяют пользователям эффективно управлять данными об оборудовании, его параметрами и предупреждениями через API.


## Images 
API ROOT 
![image](https://github.com/Kana-afk/roboguard/assets/73513054/73cb6814-dddd-4722-8106-c2572da732e9)
Swagger 
![image](https://github.com/Kana-afk/roboguard/assets/73513054/6f8e7e65-20d0-4b11-bdbd-9abb8990fa55)
![image](https://github.com/Kana-afk/roboguard/assets/73513054/c6f2347f-670f-4ce6-8baf-e26e720774e5)
Redoc 
![image](https://github.com/Kana-afk/roboguard/assets/73513054/c3cae646-308c-4237-87e8-31282f0ae6d4)
![image](https://github.com/Kana-afk/roboguard/assets/73513054/ee059b46-d78c-4872-8964-fec66270bbc3)







