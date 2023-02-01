from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView
from users.apps import UsersConfig
from users.views import CustomLoginView, UserEditProfileView, CustomRegisterView
from users.views import EmailVerify

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='users/invalid_verify.html'),
        name='invalid_verify'
    ),

    path(
        'verify_email/<uidb64>/<token>/',
        EmailVerify.as_view(),
        name='verify_email',
    ),

    path(
        'confirm_email/',
        TemplateView.as_view(template_name='users/confirm_email.html'),
        name='confirm_email'
    ),
]