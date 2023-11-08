from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from school.permissions import IsModerator, IsOwner

from school.models import Kurs, Lesson, Pay
from school.serializers import KursSerializer, LessonSerializer, PaySerializer, LessonListSerializer


# Create your views here.
class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerializer
    queryset = Kurs.objects.all()

    def get_permissions(self):
        action_permissions = {
            'retrieve': [IsOwner | IsModerator | IsAdminUser],
            'create': [IsAdminUser],
            'destroy': [IsOwner | IsAdminUser],
            'update': [IsOwner | IsModerator | IsAdminUser],
        }

        default_permissions = [IsAuthenticated]

        return [permission() for permission in action_permissions.get(self.action, default_permissions)]




class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsAdminUser]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsAdminUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]





class PayListAPIView(generics.ListAPIView):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('kurspay', 'lessonpay', 'paymentmethod',)
    ordering_fields = ('datapay',)
    permission_classes = [IsAuthenticated]