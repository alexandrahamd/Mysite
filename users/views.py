from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView, CreateView
from django.conf import settings
from users.forms import UserEditForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    # form_class = UserCreationForm


class UserEditView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserEditForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user


class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/user_form.html'


    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.email = form.cleaned_data['email']
            title = 'Проверка почты'
            body = 'Проверка почты для сайта'
            try:
                send_mail(
                    title,
                    body,
                    settings.EMAIL_HOST_USER,
                    self.object.email,
                    fail_silently=False,
                )
                self.object.save()
            except:
                Exception
            self.object.save()
        return super().form_valid(form)
