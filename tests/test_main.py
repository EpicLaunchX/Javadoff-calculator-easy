from unittest.mock import patch

import pytest

from src.pytemplate.entrypoints.cli.main import main


def test_main_add():
    with patch("builtins.input", side_effect=["1", "2", "add"]):
        result = main()
        assert result == 3


def test_main_subtract():
    with patch("builtins.input", side_effect=["1", "2", "subtract"]):
        result = main()
        assert result == -1


def test_main_multiply():
    with patch("builtins.input", side_effect=["1", "2", "multiply"]):
        result = main()
        assert result == 2


def test_main_divide():
    with patch("builtins.input", side_effect=["2", "1", "divide"]):
        result = main()
        assert result == 2
