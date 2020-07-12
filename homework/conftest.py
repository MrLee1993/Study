# -*- coding： utf-8 -*-
import pytest


@pytest.fixture(scope='module')
def count():
    print("\n开始计算")
    yield
    print("\n计算结束")
