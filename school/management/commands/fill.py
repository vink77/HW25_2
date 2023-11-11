from django.core.management.base import BaseCommand
import json
from school.models import Kurs, Lesson, Pay
from users.models import User
class Command(BaseCommand):

    def handle(self, *args, **options):
        #Очищаем БД
        User.objects.all().delete()
        Kurs.objects.all().delete()
        Lesson.objects.all().delete()
        Pay.objects.all().delete()


        with open('school/data_json/data_users.json', 'r', encoding='UTF-8') as us:
            users_to_fill = json.load(us)
            for item in users_to_fill:
                User.objects.create(
                    pk=item['pk'],
                    email=item['fields']['email'],
                    phone=item['fields']['phone'],
                    city=item['fields']['city'],
                    avatar=item['fields']['avatar'],
                    is_staff=item['fields']['is_staff'],
                    is_superuser=item['fields']['is_superuser'],
                )


        with open('school/data_json/data_kurs.json', 'r', encoding='UTF-8') as kr:
            kurs_to_fill = json.load(kr)
            for item in kurs_to_fill:
                userd = User.objects.get(pk=item['fields']['user'])
                Kurs.objects.create(
                    pk=item['pk'],
                    kurs_name=item['fields']['kurs_name'],
                    kurs_avatar=item['fields']['kurs_avatar'],
                    user=userd,
                    kurs_description=item['fields']['kurs_description'],
                    )

        with open('school/data_json/data_lesson.json', 'r', encoding='UTF-8') as ls:
            lesson_to_fill = json.load(ls)
            for item in lesson_to_fill:
                userg = User.objects.get(pk=item['fields']['user'])
                kursg = Kurs.objects.get(pk=item['fields']['kurs'])
                Lesson.objects.create(
                    pk=item['pk'],
                    lesson_name=item['fields']['lesson_name'],
                    lesson_avatar=item['fields']['lesson_avatar'],
                    lesson_description=item['fields']['lesson_description'],
                    video_url=item['fields']['video_url'],
                    kurs=kursg,
                    user=userg,
                )

            with open('school/data_json/data_pay.json', 'r', encoding='UTF-8') as py:
                pay_to_fill = json.load(py)
                for item in pay_to_fill:
                    user = User.objects.get(pk=item['fields']['user'])
                    kurspays = Kurs.objects.get(pk=item['fields']['kurspay'])
                    lessonpays = Lesson.objects.get(pk=item['fields']['lessonpay'])

                    Pay.objects.create(
                        pk=item['pk'],
                        user=user,
                        datapay=item['fields']['datapay'],
                        kurspay=kurspays,
                        lessonpay=lessonpays,
                        payment=item['fields']['payment'],
                        paymentmethod=item['fields']['paymentmethod']
                    )
