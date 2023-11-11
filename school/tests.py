from django.test import TestCase

# Create your tests here.
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson, Kurs
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
            kurs=self.kurs,
            user=self.user
        )

    def test_getting_lesson_list(self):
        response = self.client.get(
            reverse('school:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            json.loads(response.body),
            [
                {
                    'id': self.lesson.id,
                    'lesson_name': self.lesson.lesson_name,
                    'lesson_avatar':None,
                    'lesson_description': self.lesson.lesson_description,
                    'video_url': None,
                    'kurs': None,
                    'user':None,
                }
            ]
        )

    def test_create_lesson(self):
        data = {
            'lesson_name': 'lesson_name test create',
            'lesson_description': 'lesson_description test create'
        }

        response = self.client.post(
            reverse('/lesson/create/'),
            data
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
                'video_url': None,
                'kurs': None,
                'user': None
            }
        )

    def test_update_lesson(self):
        data = {
            'lesson_name': 'lesson_name update test',
        }

        response = self.client.patch(
            reverse('lesson/update/', args=[self.lesson.pk]),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()

        self.assertEqual(
            self.lesson.lesson_name,
            data['lesson_name update test']
        )

    def test_delete_lesson(self):
        response = self.client.delete(reverse('school:lesson-delete', kwargs={'pk': self.lesson.pk}))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
