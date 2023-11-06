from django.contrib import admin

# Register your models here.
from django.contrib import admin

from users.models import User

#admin.site.unregister(User)

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city', 'password', 'avatar',)
    list_filter = ('email', 'city',)