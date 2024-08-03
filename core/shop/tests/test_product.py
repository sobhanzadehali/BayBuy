import pytest
from ..models import Product
from helpers.test import *


@pytest.mark.django_db
def test_product_model(product_fixture, seller_fixture):
    product_object = product_fixture
    assert isinstance(product_object, Product)
    assert product_object.name == 'Product 1'
    assert product_object.description == 'Product 1 is awesome'
    assert product_object.price == 100
    assert product_object.seller_id == seller_fixture
    assert seller_fixture.is_seller == True

