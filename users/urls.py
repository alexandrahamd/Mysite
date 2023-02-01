# from django.contrib.auth.views import LogoutView
# from django.urls import path
# from users.apps import UsersConfig
# from users.views import UserLoginView, UserEditView, UserRegisterView
#
# app_name = UsersConfig.name
#
# urlpatterns = [
#     path('', UserLoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('register/', UserRegisterView.as_view(), name='register'),
#     path('profile/', UserEditView.as_view(), name='profile'),
# ]
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import CustomLoginView, UserEditProfileView, CustomRegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
]