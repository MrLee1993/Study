# -*- coding： utf-8 -*-
# 这是测试计算器的代码

import pytest
import yaml
import sys

print(sys.path.append('..'))
from pythoncode.calc import Calculator
from decimal import Decimal


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()

    # 执行加法用例
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("./add_data.yml")))
    def test_add(self, count, a, b, result):
        assert result == self.cal.add(a, b)

    # 执行减法用例
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("./sub_data.yml")))
    def test_sub(self, count, a, b, result):
        assert result == self.cal.sub(a, b)

    # 执行乘法用例
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("./mul_data.yml")))
    def test_mul(self, count, a, b, result):
        assert result == self.cal.mul(a, b)

    # 执行除法用例
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("./div_data.yml")))
    def test_div(self, count, a, b, result):
        assert result == self.cal.div(a, b)
