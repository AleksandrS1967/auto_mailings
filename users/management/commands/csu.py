from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@rambler.ru',
            first_name='Admin',
            last_name='Aleksandr',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('1234')
        user.save()
