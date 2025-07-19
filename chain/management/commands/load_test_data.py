import datetime
import random

from django.core.management.base import BaseCommand
from chain.models import LinkChain, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()  # Удаляем старые продукты
        LinkChain.objects.all().delete()  # Удаляем старые узлы

        # Создаём одного поставщика
        supplier = LinkChain.objects.create(
            name='Завод #1',
            email='supplier@example.com',
            country='Россия',
            city='Москва',
            street='Ленинградский проспект',
            house_number='15к1',
            debt=0
        )

        # Список городов РФ для ритейлеров/ИП
        russian_cities = ['Санкт-Петербург', 'Казань', 'Новосибирск']
        russian_streets = ['Невский проспект', 'Баумана', 'Красный проспект']
        russian_houses = ['10', '8а', '25']

        # Текущая дата
        today = datetime.date.today()
        current_year = today.year
        current_month = today.month

        for i in range(1, 4):
            node = LinkChain.objects.create(
                name=f'Розничная сеть #{i}',
                email=f'retailer{i}@example.com',
                country='Россия',
                city=russian_cities[i - 1],
                street=russian_streets[i - 1],
                house_number=russian_houses[i - 1],
                debt=random.randint(100, 500),
                supplier=supplier
            )

            Product.objects.create(
                name=f'Product {i}-1',
                model=f'Model_{i}1',
                release_date=today,
                link_chain=node
            )

            day = today.day - 1 if today.day > 1 else today.day + 1
            same_month_date = datetime.date(current_year, current_month, day)

            Product.objects.create(
                name=f'Product {i}-2',
                model=f'Model_{i}2',
                release_date=same_month_date,
                link_chain=node
            )

            other_month = (
                current_month - 1 if current_month > 1
                else current_month + 1
            )
            other_date = datetime.date(current_year, other_month, 15)

            Product.objects.create(
                name=f'Product {i}-3',
                model=f'Model_{i}3',
                release_date=other_date,
                link_chain=node
            )

        # Добавляем зарубежные звенья
        foreign_data = [
            ('Retail Germany', 'Германия', 'Берлин', 'Unter den Linden', '7'),
            ('Retail China', 'Китай', 'Пекин', 'Chang’an Avenue', '101'),
            ('Retail USA', 'США', 'Нью-Йорк', '5th Avenue', '350'),
        ]

        for i, (name, country, city, street, house) in enumerate(foreign_data,
                                                                 start=4):
            node = LinkChain.objects.create(
                name=name,
                email=f'{name.lower().replace(" ", "")}@example.com',
                country=country,
                city=city,
                street=street,
                house_number=house,
                debt=random.randint(200, 600),
                supplier=None
            )

            for j in range(1, 4):
                Product.objects.create(
                    name=f'Product {i}-{j}',
                    model=f'Model_{i}{j}',
                    release_date=today - datetime.timedelta(days=j),
                    link_chain=node
                )

        self.stdout.write(self.style.SUCCESS(
            'Тестовые данные успешно загружены'))
