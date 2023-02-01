from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватарка', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='номер телефона', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.username
