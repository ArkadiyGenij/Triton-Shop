import os
from io import BytesIO
from random import choice, randint, uniform

import django
from PIL import Image
from django.core.files import File
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from shop.models import Product, Category

fake = Faker('ru_RU')


def generate_fake_image():
    """Генерация тестового изображения"""
    image = Image.new('RGB', (800, 600), color=(randint(0, 255), randint(0, 255), randint(0, 255)))
    image_io = BytesIO()
    image.save(image_io, format='JPEG')
    return File(image_io, name=f'{fake.word()}.jpg')


def create_fake_products(count=30):
    """Создание тестовых товаров"""
    categories = []
    for _ in range(5):
        category, created = Category.objects.get_or_create(
            name=fake.word().capitalize(),
            defaults={'slug': fake.slug()}
        )
        categories.append(category)

    for _ in range(count):
        name = f"{fake.word().capitalize()} {fake.word().capitalize()}"

        product = Product.objects.create(
            name=name,
            category=choice(categories),
            slug=fake.slug(),
            description=fake.text(max_nb_chars=200),
            price=round(uniform(100, 10000), 2),
        )

        if randint(1, 10) <= 8:
            product.image.save(
                f'{fake.word()}.jpg',
                generate_fake_image()
            )
            product.save()

        print(f'Создан товар: {product.name}')


if __name__ == '__main__':
    print('Начало генерации тестовых товаров...')
    create_fake_products()
    print('Генерация завершена!')
