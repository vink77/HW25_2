from django.conf.urls.static import static
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from config import settings
from users.views import ProfileView, RegisterUser, PasswordRecoveryView
from users.apps import UsersConfig


app_name = 'user'


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    #path('login/', LoginView.as_view(), name='login'),
    path('password_recovery/', PasswordRecoveryView.as_view(), name='password_recovery'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)