from django.contrib.auth import get_user_model
import pytest

User = get_user_model()


# Create your tests here.


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_superuser('09380456987', 'password', )
    assert user.is_superuser == True
    assert user.is_staff == True
    assert user.is_active == True
    print(user.phone)
    print(user.is_superuser)
    assert user.phone == '09380456987'
