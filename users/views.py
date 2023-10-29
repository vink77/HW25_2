from django.shortcuts import render

# Create your views here.
import random

from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import UserRegisterForm, UserProfileForm, PasswordRecoveryForm
from users.models import User


class RegisterUser(CreateView):
    """
    Контроллер формы регистрации пользователя
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляю с регистрацией',
            message='Вы зарегистрировались на нашей платформе!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        user = form.save()
        login(self.request,user)
        return redirect('client:client_list')

class ProfileView(LoginRequiredMixin, UpdateView):
    """
    Контроллер формы профиля пользователя
    """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """
        Позволяет делать необязательным передачу pk объекта
        """
        return self.request.user

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'client/client_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('client:list')

    def logout_user(self):
        logout(self)
        return redirect('client:list')

class PasswordRecoveryView(FormView):
    template_name = 'users/password_recovery.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        password = str(random.randrange(10000, 99999, 1))
        user.set_password(password)
        user.save()
        subject = 'Восстановление пароля'
        message = f'Новый пароль: {password}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)