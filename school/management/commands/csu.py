from django.core.management.base import BaseCommand
from users.models import User
class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='vink.av@mail.ru',
            first_name='Алексей',
            last_name='Винк',
            is_staff=True,
            is_superuser=True,

        )

        user.set_password('0000')
        user.save()