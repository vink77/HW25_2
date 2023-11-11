from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from school.models import Kurs, Lesson, Pay, Subscription
from school.validators import Video_Url_Validator


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
     validators = [Video_Url_Validator(field='video_url')]

     class Meta:
         model = Lesson
         fields ='__all__'


class LessonListSerializer(serializers.ModelSerializer):
    kurs = SlugRelatedField(slug_field="kurs_name", queryset=Kurs.objects.all())
   # user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = Lesson
        #fields =("kurs_name","kurs")

        fields ='__all__'


class PaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pay
        fields ='__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'