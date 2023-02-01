from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomEditUserForm
from users.models import User
from users.models import create_new_password


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomRegisterView(CreateView):
    model = User
    form_class = UserCreationForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = create_new_password()


    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.set_password(form.data.get('password'))
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
                self.object.is_active = True
                self.object.save()
            except:
                Exception
            self.object.save()
        return super().form_valid(form)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user
