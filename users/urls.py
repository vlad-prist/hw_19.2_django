from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from users.apps import UsersConfig
from users.views import UserCreateView, UserUpdateView, email_verification, GeneratePasswordView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('generate-password/', GeneratePasswordView.as_view(
        template_name='users/generate_password.html'), name='generate-password'),
    path('generate-password/done/', GeneratePasswordView.as_view(
        template_name='users/generate_password_done.html'), name='generate-password-done'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),

]
