from rest_framework import serializers

from school.models import Kurs, Lesson


class KursSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kurs
        fields ='__all__'

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields ='__all__'