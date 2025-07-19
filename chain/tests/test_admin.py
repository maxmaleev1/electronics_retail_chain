from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase

from chain.admin import LinkChainAdmin
from chain.models import LinkChain


class MockRequest:
    """Мок-запрос от суперпользователя для передачи в ModelAdmin."""
    user = get_user_model()(is_superuser=True, is_staff=True)


class LinkChainAdminTest(TestCase):
    """Тестирование действий в админке для модели LinkChain."""

    def setUp(self):
        """Создание объекта цепи."""

        self.obj = LinkChain.objects.create(
            name='Test Chain',
            city='Москва',
            country='Россия',
            debt=1000
        )
        self.modeladmin = LinkChainAdmin(LinkChain, admin.site)
        self.request = RequestFactory().get('/')
        self.request.user = get_user_model().objects.create_superuser(
            username='admin', password='1234'
        )
