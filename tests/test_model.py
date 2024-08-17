import pytest

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.service.calculator import Calculator


def test_operands():
    operands = Operands(1, 2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2


def test_operands_factory():
    operands = operands_factory(1, 2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2


def test_calculator_add():
    calculator = Calculator()
    operands = operands_factory(1, 2)
    assert calculator.add(operands) == 3


def test_calculator_subtract():
    calculator = Calculator()
    operands = operands_factory(1, 2)
    assert calculator.subtract(operands) == -1


def test_calculator_multiply():
    calculator = Calculator()
    operands = operands_factory(1, 2)
    assert calculator.multiply(operands) == 2


def test_calculator_divide():
    calculator = Calculator()
    operands = operands_factory(2, 1)
    assert calculator.divide(operands) == 2
