import pytest

from src.pytemplate.domain.models import Operands


def test_operands():
    operands = Operands(1, 2)
    assert operands.first_operand == 1
    assert operands.second_operand == 2
