from django.db import models

from users.models import NULLABLE


# Create your models here.
class Kurs(models.Model):
    kurs_name = models.CharField(max_length=100, verbose_name='название курса')
    kurs_avatar = models.ImageField(upload_to='school/', verbose_name='картинка', **NULLABLE)
    kurs_description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.kurs_name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100, verbose_name='название урока')
    lesson_avatar = models.ImageField(upload_to='school/', verbose_name='картинка урока', **NULLABLE)
    lesson_description = models.TextField(**NULLABLE, verbose_name='описание урока')
    video_url = models.URLField( **NULLABLE, verbose_name='ссылка на видео')


    def __str__(self):
        return f'{self.lesson_name} '

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'