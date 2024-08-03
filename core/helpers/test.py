import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from shop.models import Product, Category, Comment, Coupon

User = get_user_model()


@pytest.fixture()
def category_fixture():
    return Category.objects.create(name='Category 1')


@pytest.fixture()
def seller_fixture():
    return User.objects.create_user('09380456987', 'password', is_seller=True)


@pytest.fixture()
def product_fixture(seller_fixture, category_fixture):
    return Product.objects.create(name='Product 1', seller_id=seller_fixture, category_id=category_fixture,
                                  price=100, in_stock=10, description='Product 1 is awesome')


@pytest.fixture()
def coupon_fixture():
    return Coupon.objects.create(coupon_code='Coupon 1', percent=35,
                                 expiration_date=timezone.now() + timezone.timedelta(days=30),
                                 description='Coupon 1 is awesome')
