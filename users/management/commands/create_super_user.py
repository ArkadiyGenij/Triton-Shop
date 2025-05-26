from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@test.test',
            first_name='Test',
            last_name='Test',
            is_superuser=True,
            is_staff=True,
        )
        user.set_password('123qwe456rty')
        user.save()
