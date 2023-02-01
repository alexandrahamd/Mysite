from django.contrib.auth.forms import UserChangeForm
from users.models import User


class CustomEditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar',)