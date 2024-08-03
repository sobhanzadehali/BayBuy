from helpers.test import *
from shop.models import CouponBuyerProduct
import pytest


@pytest.mark.django_db
def test_coupon(coupon_fixture, seller_fixture, product_fixture):
    coupon_id = coupon_fixture
    buyer_id = seller_fixture
    product_id = product_fixture
    cp_object = CouponBuyerProduct.objects.create(coupon_id=coupon_id, buyer_id=buyer_id, product_id=product_id)
    assert isinstance(CouponBuyerProduct.objects.get(coupon_id=coupon_id), CouponBuyerProduct)
    assert cp_object.coupon_id.coupon_code == 'Coupon 1'
    assert cp_object.coupon_id.expiration_date == coupon_fixture.expiration_date
