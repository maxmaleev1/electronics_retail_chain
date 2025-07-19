import base64
from django.contrib.auth.models import User
from chain.models import LinkChain
from rest_framework.test import APIClient, APITestCase


class LinkChainAPITest(APITestCase):
    """Тесты API для модели звена цепи поставок (LinkChain)."""

    def setUp(self):
        self.user = User.objects.create_user(username='active',
                                             password='1234')
        self.inactive_user = User.objects.create_user(
            username='inactive', password='1234', is_active=False
        )

        self.client = APIClient()
        credentials = base64.b64encode(b'active:1234').decode('utf-8')
        self.client.credentials(HTTP_AUTHORIZATION=f'Basic {credentials}')

        self.node = LinkChain.objects.create(
            name='Звено 1',
            email='zveno@example.com',
            country='Россия',
            city='Москва',
            street='Ленинa',
            house_number='10',
            debt=500.00,
        )

    def test_auth_required(self):
        """Неавторизованный пользователь получает 403."""
        self.client.logout()
        res = self.client.get('/chain/links/')
        self.assertEqual(res.status_code, 401)

    def test_inactive_user_forbidden(self):
        """Неактивный пользователь получает 403."""
        self.client.logout()
        self.client.login(username='inactive', password='1234')
        res = self.client.get('/chain/links/')
        self.assertEqual(res.status_code, 401)

    def test_list_links(self):
        """Получение списка звеньев цепи."""
        res = self.client.get('/chain/links/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)

    def test_retrieve_link(self):
        """Получение одного звена по ID."""
        res = self.client.get(f'/chain/links/{self.node.id}/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['name'], 'Звено 1')

    def test_filter_by_country(self):
        """Фильтрация звеньев по стране."""
        res = self.client.get('/chain/links/?country=Россия')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()[0]['country'], 'Россия')

    def test_create_link(self):
        """Создание нового звена."""
        data = {
            'name': 'Новое звено',
            'email': 'new@example.com',
            'country': 'Китай',
            'city': 'Пекин',
            'street': 'Центральная',
            'house_number': '88'
        }
        res = self.client.post('/chain/links/', data)
        self.assertEqual(res.status_code, 201)
        self.assertTrue(LinkChain.objects.filter(name='Новое звено').exists())

    def test_update_link_without_debt(self):
        """Обновление звена без изменения поля 'debt'."""
        data = {
            'name': 'Обновлённое звено',
            'email': 'zveno@example.com',
            'country': 'Россия',
            'city': 'Москва',
            'street': 'Ленина',
            'house_number': '10',
            'debt': 0  # должен игнорироваться
        }
        res = self.client.put(f'/chain/links/{self.node.id}/', data)
        self.assertEqual(res.status_code, 200)
        self.node.refresh_from_db()
        self.assertEqual(self.node.name, 'Обновлённое звено')
        self.assertEqual(float(self.node.debt), 500.00)

    def test_partial_update(self):
        """Частичное обновление (например, только город)."""
        res = self.client.patch(f'/chain/links/{self.node.id}/',
                                {'city': 'Казань'})
        self.assertEqual(res.status_code, 200)
        self.node.refresh_from_db()
        self.assertEqual(self.node.city, 'Казань')

    def test_delete_link(self):
        """Удаление звена цепи."""
        res = self.client.delete(f'/chain/links/{self.node.id}/')
        self.assertEqual(res.status_code, 204)
        self.assertFalse(LinkChain.objects.filter(id=self.node.id).exists())
