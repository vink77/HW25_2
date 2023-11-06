from django.db import models

from users.models import NULLABLE, User


# Create your models here.
class Kurs(models.Model):
    kurs_name = models.CharField(max_length=100, verbose_name='название курса')
    kurs_avatar = models.ImageField(upload_to='school/', verbose_name='картинка', **NULLABLE)
    kurs_description = models.TextField(**NULLABLE, verbose_name='описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)


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
    kurs = models.ForeignKey(Kurs, related_name='lesson', on_delete=models.SET_NULL, **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)


    def __str__(self):
        return f'{self.lesson_name} '

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

class Pay(models.Model):

    METHOD_TRANS = 'transfer'
    METHOD_CASH = 'cash'
    PAI_METHOD = (

        (METHOD_TRANS, 'перевод на счет'),
        (METHOD_CASH, 'наличными'),
    )

    user = models.ForeignKey(User,related_name='user', on_delete=models.SET_NULL, **NULLABLE)
    datapay = models.DateTimeField(verbose_name='дата оплаты', **NULLABLE)
    kurspay = models.ForeignKey(Kurs,related_name='kurspay', on_delete=models.SET_NULL, verbose_name='оплата курса', **NULLABLE)
    lessonpay = models.ForeignKey(Lesson,related_name='lessonpay', on_delete=models.SET_NULL,verbose_name='оплата урока', **NULLABLE)
    payment = models.FloatField(verbose_name='сумма оплаты', **NULLABLE)
    paymentmethod = models.CharField(max_length=35, choices=PAI_METHOD, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} ({self.payment})'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'