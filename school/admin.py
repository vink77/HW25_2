from django.contrib import admin

# Register your models here.
from django.contrib import admin
from school.models import Kurs, Lesson, Pay
from users.models import User
# Register your models here.
#admin.site.register(Category)

#admin.site.register(User)

@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ('kurs_name','kurs_avatar','kurs_description', 'user',)
    list_filter = ('kurs_name',)
    search_fields = ('kurs_name', 'pk','user',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'lesson_avatar', 'lesson_description', 'video_url', 'kurs', 'user')
    search_fields = ('lesson_name', 'kurs', 'user')

 #   def clients(self, obj):
#        return ', '.join([client.email for client in obj.mailing_clients.all()])
#
#    clients.short_description = 'Message Clients'

@admin.register(Pay)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'datapay', 'kurspay', 'lessonpay', 'payment', 'paymentmethod')
    search_fields = ('user', 'datapay', 'kurspay')