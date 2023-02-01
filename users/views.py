from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomEditUserForm, CustomUserCreationForm, UserAuthenticationForm
from users.models import User
from users.models import create_new_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as \
    token_generator

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserAuthenticationForm


class CustomRegisterView(CreateView):
    template_name = 'users/user_form.html'
    form_class = CustomUserCreationForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = create_new_password()

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         self.object.is_active = False
    #         self.object.set_password(form.data.get('password'))
    #         self.object.email = form.cleaned_data['email']
    #         title = 'Проверка почты'
    #         body = 'Проверка почты для сайта'
    #         try:
    #             send_mail(
    #                 title,
    #                 body,
    #                 settings.EMAIL_HOST_USER,
    #                 self.object.email,
    #                 fail_silently=False,
    #             )
    #             self.object.is_active = True
    #             self.object.save()
    #         except:
    #             Exception
    #         self.object.save()
    #     return super().form_valid(form)
    # def form_valid(self, form, self=None):
    #     if form.is_valid():
    #         self.object = form.save()
    #         self.object.is_active = False
    #         self.object.set_password(form.data.get('password'))
    #         self.object.email = form.cleaned_data['email']
    #         send_register_mail(
    #             subject='Активация'
    #             message=f'http/localhost:8080/users/activate/{self.object.token}'
    #         )
    #     return super().form_valid(form)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user
