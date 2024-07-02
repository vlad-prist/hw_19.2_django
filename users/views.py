from random import choice

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
import secrets


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет! Перейди по ссылке для подтверждения почти {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('catalog:categories_list') # Переход на "Главную"страницу после редактирования пользователя


class GeneratePasswordView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/generate.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        if user:
            password = User.objects.make_random_password(length=10)
            # password = ''.join([choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(7)])
            user.set_password(password)
            user.save()
            send_mail(
                subject='Изменение пароля',
                message=f'Ваш новый пароль: {password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
        return redirect(reverse('users:generate-password-done'))
