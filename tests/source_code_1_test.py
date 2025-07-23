import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from source_code_1 import *


import pytest
from source_code import add_numbers, subtract_numbers, divide_numbers, is_even, Calculator

class TestMathFunctions:
    def test_add_numbers_valid_input(self):
        assert add_numbers(2, 3) == 5
        assert add_numbers(10.5, 2.5) == 13.0
        assert add_numbers(0, 0) == 0

    def test_add_numbers_invalid_input(self):
        with pytest.raises(TypeError):
            add_numbers("a", 2)
        with pytest.raises(TypeError):
            add_numbers(2, "b")
        with pytest.raises(TypeError):
            add_numbers("a", "b")

    def test_subtract_numbers_valid_input(self):
        assert subtract_numbers(5, 3) == 2
        assert subtract_numbers(10.5, 2.5) == 8.0
        assert subtract_numbers(0, 0) == 0

    def test_subtract_numbers_invalid_input(self):
        with pytest.raises(TypeError):
            subtract_numbers("a", 2)
        with pytest.raises(TypeError):
            subtract_numbers(2, "b")

    def test_divide_numbers_valid_input(self):
        assert divide_numbers(6, 3) == 2.0
        assert divide_numbers(10.5, 2.5) == 4.2
        assert divide_numbers(10, 2) == 5.0

    def test_divide_numbers_zero_division(self):
        with pytest.raises(ValueError):
            divide_numbers(5, 0)

    def test_divide_numbers_invalid_input(self):
        with pytest.raises(TypeError):
            divide_numbers("a", 2)
        with pytest.raises(TypeError):
            divide_numbers(2, "b")


    def test_is_even_valid_input(self):
        assert is_even(2) == True
        assert is_even(0) == True
        assert is_even(-4) == True

    def test_is_even_invalid_input(self):
        with pytest.raises(TypeError):
            is_even(2.5)
        with pytest.raises(TypeError):
            is_even("2")


class TestCalculator:
    def test_calculator_add(self):
        calc = Calculator()
        assert calc.calculate("add", 2, 3) == 5
        assert calc.get_history() == ['2 add 3 = 5']

    def test_calculator_subtract(self):
        calc = Calculator()
        assert calc.calculate("subtract", 5, 2) == 3
        assert calc.get_history() == ['5 subtract 2 = 3']

    def test_calculator_divide(self):
        calc = Calculator()
        assert calc.calculate("divide", 6, 3) == 2.0
        assert calc.get_history() == ['6 divide 3 = 2.0']

    def test_calculator_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.calculate("divide", 5, 0)

    def test_calculator_invalid_operation(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.calculate("multiply", 2, 3)

    def test_calculator_invalid_input(self):
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.calculate("add", "a", 2)
        with pytest.raises(TypeError):
            calc.calculate("add", 2, "b")

    def test_calculator_history(self):
        calc = Calculator()
        calc.calculate("add", 2, 3)
        calc.calculate("subtract", 5, 2)
        assert calc.get_history() == ['2 add 3 = 5', '5 subtract 2 = 3']

