import random
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as \
    token_generator


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string(
        'users/verify_email.html',
        context=context,
    )
    email = EmailMessage(
        'Veryfi email',
        message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )
    email.send()


def create_new_password():
    alphas = "abcdefghijklmnopqrstuvwxyz"
    alphas_cap = alphas.upper()
    numbers = "12345678901234567890123456"
    special_chars = "!@#$%^&*()_+/!@#$%^&*()_+/"
    password_characters = [alphas, alphas_cap, numbers, special_chars]
    new_password = ""
    for i in range(16):
        n = random.randint(0, 3)
        chars_used = password_characters[n]
        char = chars_used[random.randint(0, 25)]
        new_password += char
    return new_password