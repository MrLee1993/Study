# -*- coding： utf-8 -*-
import pytest
import sys

print(sys.path.append('..'))
from pythoncode.calc import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("\nsetup")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 2),
        (2, 2, 4),
        (3, 4, 8)
    ])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self):
        assert 3 == self.cal.add(2, 1)

    @pytest.mark.div
    def test_div(self):
        assert 1 == self.cal.div(1, 1)

    def teardown_class(self):
        print("\ntearup")
