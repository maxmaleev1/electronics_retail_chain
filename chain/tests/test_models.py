from django.test import TestCase
from chain.models import LinkChain


class LinkChainModelTest(TestCase):
    """Тестирование модели LinkChain."""

    def test_str_representation(self):
        """Проверка метода __str__."""
        obj = LinkChain.objects.create(
            name='Shop1', city='Москва', country='Россия', debt=100
        )
        self.assertEqual(str(obj), 'Shop1 — Москва (Россия)')
