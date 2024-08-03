from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import CustomUser


# for admin page
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('phone', 'fname', 'lname', 'is_seller')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('phone', 'is_seller')
