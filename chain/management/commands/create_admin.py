from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Создаёт суперпользователя admin с паролем 1234'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='1234'
            )
            self.stdout.write(self.style.SUCCESS(
                '✅ Суперпользователь admin создан.'))
        else:
            self.stdout.write(self.style.WARNING(
                '⚠️ Пользователь admin уже существует.'))
