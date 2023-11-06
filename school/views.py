from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from school.models import Kurs, Lesson, Pay
from school.serializers import KursSerializer, LessonSerializer, PaySerializer


# Create your views here.
class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerializer
    queryset = Kurs.objects.all()





class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()




class PayListAPIView(generics.ListAPIView):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('kurspay', 'lessonpay', 'paymentmethod',)
    ordering_fields = ('datapay',)