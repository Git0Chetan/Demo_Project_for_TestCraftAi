import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from source_code_1 import *


import pytest
from your_module import add_numbers, subtract_numbers, divide_numbers, is_even, Calculator  # Replace your_module

# Tests for add_numbers
def test_add_numbers_integers():
    assert add_numbers(2, 3) == 5

def test_add_numbers_floats():
    assert add_numbers(2.5, 3.5) == 6.0

def test_add_numbers_mixed():
    assert add_numbers(2, 3.5) == 5.5

def test_add_numbers_invalid_input():
    with pytest.raises(TypeError):
        add_numbers("2", 3)

def test_add_numbers_invalid_input2():
    with pytest.raises(TypeError):
        add_numbers(2, "3")


# Tests for subtract_numbers
def test_subtract_numbers_integers():
    assert subtract_numbers(5, 3) == 2

def test_subtract_numbers_floats():
    assert subtract_numbers(5.5, 2.5) == 3.0

def test_subtract_numbers_mixed():
    assert subtract_numbers(5, 2.5) == 2.5

def test_subtract_numbers_invalid_input():
    with pytest.raises(TypeError):
        subtract_numbers("5", 3)

# Tests for divide_numbers
def test_divide_numbers_integers():
    assert divide_numbers(6, 3) == 2.0

def test_divide_numbers_floats():
    assert divide_numbers(6.0, 3.0) == 2.0

def test_divide_numbers_mixed():
    assert divide_numbers(6, 3.0) == 2.0

def test_divide_numbers_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(6, 0)

def test_divide_numbers_invalid_input():
    with pytest.raises(TypeError):
        divide_numbers("6", 3)

# Tests for is_even
def test_is_even_even():
    assert is_even(4) == True

def test_is_even_odd():
    assert is_even(5) == False

def test_is_even_invalid_input():
    with pytest.raises(TypeError):
        is_even(4.5)

# Tests for Calculator class
def test_calculator_add():
    calc = Calculator()
    assert calc.calculate("add", 2, 3) == 5
    assert "2 add 3 = 5" in calc.get_history()

def test_calculator_subtract():
    calc = Calculator()
    assert calc.calculate("subtract", 5, 2) == 3
    assert "5 subtract 2 = 3" in calc.get_history()

def test_calculator_divide():
    calc = Calculator()
    assert calc.calculate("divide", 6, 3) == 2.0
    assert "6 divide 3 = 2.0" in calc.get_history()

def test_calculator_unsupported_operation():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate("multiply", 2, 3)

def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate("divide", 6,0)

def test_calculator_invalid_input():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.calculate("add", "2", 3)

