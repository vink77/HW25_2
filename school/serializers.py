from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from school.models import Kurs, Lesson, Pay
from users.models import User


class KursSerializer(serializers.ModelSerializer):
    lesson_counter = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    class Meta:
        model = Kurs
        fields ='__all__'


    # Вывод поля уроков курса
    def get_lessons(self, course):
        return [lesson.name for lesson in course.lesson.all()]

    # Вывод количества уроков в курсе
    def get_lesson_counter(self, obj):
        return Lesson.objects.filter(course=obj).count()


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields ='__all__'




class LessonListSerializer(serializers.ModelSerializer):
    kurs = SlugRelatedField(slug_fields="kurs_name", queryset=Kurs.objects.all())
    user = SlugRelatedField(slug_fields="email", queryset=User.objects.all())
    class Meta:
        model = Lesson
        fields =('kurs','user')

class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields ='__all__'