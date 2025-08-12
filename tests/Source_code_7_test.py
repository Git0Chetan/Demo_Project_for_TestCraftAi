import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_7 import *


import pytest
from temp import add_numbers, subtract_numbers, divide_numbers, is_even, Calculator

# Test functions for add_numbers
def test_add_numbers_int():
    assert add_numbers(2, 3) == 5

def test_add_numbers_float():
    assert add_numbers(2.5, 3.5) == 6.0

def test_add_numbers_mixed():
    assert add_numbers(2, 3.5) == 5.5

def test_add_numbers_invalid_input():
    with pytest.raises(TypeError):
        add_numbers("2", 3)

def test_add_numbers_invalid_input2():
    with pytest.raises(TypeError):
        add_numbers(2, "3")


# Test functions for subtract_numbers
def test_subtract_numbers_int():
    assert subtract_numbers(5, 3) == 2

def test_subtract_numbers_float():
    assert subtract_numbers(5.5, 3.5) == 2.0

def test_subtract_numbers_mixed():
    assert subtract_numbers(5, 3.5) == 1.5

def test_subtract_numbers_invalid_input():
    with pytest.raises(TypeError):
        subtract_numbers("5", 3)

# Test functions for divide_numbers
def test_divide_numbers_int():
    assert divide_numbers(6, 3) == 2.0

def test_divide_numbers_float():
    assert divide_numbers(6.0, 3.0) == 2.0

def test_divide_numbers_mixed():
    assert divide_numbers(6, 3.0) == 2.0

def test_divide_numbers_by_zero():
    with pytest.raises(ValueError):
        divide_numbers(6, 0)

def test_divide_numbers_invalid_input():
    with pytest.raises(TypeError):
        divide_numbers("6", 3)


# Test functions for is_even
def test_is_even_even():
    assert is_even(4) == True

def test_is_even_odd():
    assert is_even(5) == False

def test_is_even_invalid_input():
    with pytest.raises(TypeError):
        is_even(4.5)


# Test functions for Calculator class
def test_calculator_add():
    calc = Calculator()
    assert calc.calculate("add", 2, 3) == 5
    assert calc.get_history() == ['2 add 3 = 5']

def test_calculator_subtract():
    calc = Calculator()
    assert calc.calculate("subtract", 5, 3) == 2
    assert calc.get_history() == ['5 subtract 3 = 2']

def test_calculator_divide():
    calc = Calculator()
    assert calc.calculate("divide", 6, 3) == 2.0
    assert calc.get_history() == ['6 divide 3 = 2.0']

def test_calculator_invalid_operation():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate("multiply", 2, 3)

def test_calculator_history():
    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.calculate("subtract", 5, 2)
    assert calc.get_history() == ['2 add 3 = 5', '5 subtract 2 = 3']

def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate("divide", 5, 0)

def test_calculator_invalid_input():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.calculate("add", "2", 3)

