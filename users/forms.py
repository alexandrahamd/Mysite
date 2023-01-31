from django import forms
from users.models import User
from django.contrib.auth.forms import UserChangeForm


class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'phone', 'country', )