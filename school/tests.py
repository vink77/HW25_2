from django.test import TestCase

# Create your tests here.
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson, Kurs, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test1@skypro.ru')
        self.user.set_password('1234')
        self.user.save()

        self.kurs = Kurs.objects.create(
            kurs_name='kurs_name_test',
            kurs_description='kurs_description_test',
            user=self.user)

        self.lesson = Lesson.objects.create(
            lesson_name='lesson_name_test',
            lesson_description='lesson_description_test',
            video_url= 'https://youtube.com/test/',
            kurs=self.kurs,
            user=self.user
        )

    def test_getting_lesson_list(self):
        """Тестирование вывода списка уроков"""
        response = self.client.get(
            reverse('school:lesson_list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
              'next': None,
              'previous': None,
              'results': [
                    {'id': 4,
                     'kurs': 'kurs_name_test',
                     'lesson_name': 'lesson_name_test',
                     'lesson_avatar': None,
                     'lesson_description': 'lesson_description_test',
                     'video_url': 'https://youtube.com/test/',
                     'user': 3}
                          ]
              }

            )

    def test_create_lesson(self):
        '''Тестирование создания уроков'''
        data = {
            'lesson_name': 'lesson_name test create',
            'lesson_description': 'lesson_description test create',
            'video_url': 'https://youtube.com/test/',
        }

        response = self.client.post(
            reverse('school:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            2,
            Lesson.objects.all().count()
        )
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'lesson_name': 'lesson_name test create',
                'lesson_avatar': None,
                'lesson_description': 'lesson_description test create',
                'video_url': 'https://youtube.com/test/',
                'kurs': None,
                'user': None
            }
        )
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_update_lesson(self):
        '''Тестирование изменения урока'''

        data = {
            'lesson_name': 'lesson_name update test',
            'video_url': 'https://youtube.com/test/',

        }
        url = reverse('school:lesson_update', args=[self.lesson.id])
        response = self.client.put(url, data=data, format='json'
        )


        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()
        self.assertEqual(
            self.lesson.lesson_name,
            'lesson_name update test'
        )

    def test_delete_lesson(self):
        '''Тестирование удаления урока'''

        response = self.client.delete(reverse('school:lesson_delete', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

    def test_retrieve_lesson(self):
        """Тестирование вывода одного урока"""
        response = self.client.get(reverse('school:lesson_get', args=[self.lesson.id]))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(response.json()['lesson_name'], 'lesson_name_test')

    def test_url_validator(self):
        """Тестирование валидации url"""
        data = {
            'lesson_name': 'lesson_name update test',
            'video_url': 'https://test.com/test/',

        }
        url = reverse('school:lesson_update', args=[self.lesson.id])
        response = self.client.put(url, data=data, format='json'
                                   )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create(email='test1@skypro.ru')
        self.user.set_password('1234')
        self.user.save()

        self.kurs = Kurs.objects.create(
            kurs_name='kurs_name_test',
            kurs_description='kurs_description_test',
            user=self.user)

        self.subscription = Subscription.objects.create(course=self.kurs, user=self.user)
    def test_subscribe(self):
        """Тестирование подписки на курс"""
        data = {'course': self.kurs.pk}
        url = reverse('school:subscription-list')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            response.json(),
            {'id': 2, 'is_active': False, 'course': 7, 'user': None}
        )
    def test_unsubscribe(self):
        """Тестирование cмены статуса подписки на курс"""
        data = {'is_active': True}
        url = reverse('school:subscription-detail', kwargs={'pk': self.subscription.pk})
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {'id': 3, 'is_active': True, 'course': 8, 'user': 8})
