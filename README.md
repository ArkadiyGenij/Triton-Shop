# Инструкция по запуску интернет-магазина Triton

## Установка и настройка проекта

1. **Клонирование репозитория**:
   ```bash
   git clone <ваш_репозиторий>
   cd <папка_проекта>
   ```

2. **Создание и активация виртуального окружения**:
```bash
   python -m venv venv
   # Для Windows:
   venv\Scripts\activate
   # Для Linux/MacOS:
   source venv/bin/activate
  ```

3. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка базы данных**:
   ```bash
   python manage.py migrate
   ```

## Создание суперпользователя

Для создания администратора выполните:
```bash
  python create_super_user.py
```

Данные для входа:
- Email: `test@test.test`
- Пароль: `123qwe456rty`

## Генерация тестовых данных

Для заполнения базы тестовыми товарами выполните:
```bash
  python create_test_products.py
```

## Запуск сервера

```bash
  python manage.py runserver
```

После запуска сервер будет доступен по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Основные URL-адреса

### Пользовательская часть
- Главная страница: `/`
- Вход: `/users/login/`
- Выход: `/users/logout/`
- Регистрация: `/users/register/`

### Административная часть
- Панель управления: `/dashboard/`
- Список товаров: `/dashboard/products`
- Создание товара: `/dashboard/products/create`
- Редактирование товара: `/dashboard/products/edit/<id>`
- Просмотр товара: `/dashboard/products/detail/<id>`
- Удаление товара: `/dashboard/products/delete/<id>` 

## Дополнительные команды

Создание миграций:
```bash
  python manage.py makemigrations
```

Применение миграций:
```bash
  python manage.py migrate
```

Сбор статических файлов (для production):
```bash
  python manage.py collectstatic
```

## Техническая информация

- Проект использует Django в качестве backend-фреймворка
- Для фронтенда используется Bootstrap
- Для генерации тестовых данных используется библиотека Faker
- Изображения товаров хранятся в директории `media/`

Для доступа к административной панели необходимо войти под учетной записью с правами `is_staff=True`