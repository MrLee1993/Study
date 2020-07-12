# -*- coding： utf-8 -*-
import pytest


def test_cart1(login):
    print("购物车测试用例1")


def test_cart2(login):
    print("购物车测试用例2")


# @pytest.mark .parametrize('a, b', [
#     (1,2),
#     (3,4)
# ])

@pytest.mark.parametrize('login', [
    ('username', 'password'),
    ('username1', 'password1')
], indirect=True)
def test_cart3(login):
    print("购物车测试用例3")
