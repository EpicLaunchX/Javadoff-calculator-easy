import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_operands():
    operands = Operands(1, 2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2


def test_operands_factory():
    operands = operands_factory(1, 2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2
