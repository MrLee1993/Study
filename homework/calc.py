# -*- coding： utf-8 -*-
from decimal import Decimal


# 实现计算器功能
class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

    def sub(self, a, b):
        return (Decimal(a) - Decimal(b))

    def mul(self, a, b):
        return a * b
