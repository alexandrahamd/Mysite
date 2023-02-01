from django.contrib.auth.models import AbstractUser
from django.db import models
import random

from django.shortcuts import redirect


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


class User(AbstractUser):
    # username = None
    password = models.CharField(max_length=200, default=create_new_password())
    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватарка', blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name='номер телефона', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True, null=True)
    # token = models.CharField(max_length=15, verbose_name='Токен')
    # token_created = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return redirect("catalog:home")
