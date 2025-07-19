from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Создаёт неактивного пользователя testuser с паролем 1234'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user(
                username='testuser',
                email='testuser@example.com',
                password='1234',
                is_active=False
            )
            self.stdout.write(self.style.SUCCESS(
                '✅ Неактивный пользователь testuser создан.'))
        else:
            self.stdout.write(self.style.WARNING(
                '⚠️ Пользователь testuser уже существует.'))
