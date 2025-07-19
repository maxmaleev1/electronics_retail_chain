from django.db import models


class LinkChain(models.Model):
    '''Звено сети (завод / розница / ИП)'''

    name = models.CharField(max_length=255)  # Название звена
    email = models.EmailField()  # Контактный email
    country = models.CharField(max_length=100)  # Страна
    city = models.CharField(max_length=100)  # Город
    street = models.CharField(max_length=100)  # Улица
    house_number = models.CharField(max_length=20)  # Номер дома

    supplier = models.ForeignKey(  # Поставщик (предыдущее звено)
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='clients'
    )

    debt = models.DecimalField(  # Задолженность перед поставщиком
        max_digits=12,
        decimal_places=2,
        default=0.00
    )

    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f'{self.name} — {self.city} ({self.country})'


class Product(models.Model):
    '''Продукт, поставляемый звеном сети'''

    link_chain = models.ForeignKey(  # К какому звену относится продукт
        LinkChain,
        on_delete=models.CASCADE,
        related_name='products'
    )

    name = models.CharField(max_length=255)  # Название продукта
    model = models.CharField(max_length=255)  # Модель
    release_date = models.DateField()  # Дата выхода на рынок

    def __str__(self):
        return f'{self.name} ({self.model})'
