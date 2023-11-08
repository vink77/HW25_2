from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
NULLABLE = {"null": True, "blank": True}
# Create your models here.

class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.MEMBER)




    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'