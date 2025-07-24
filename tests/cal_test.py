import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cal import *


import pytest
from source_code import add_numbers, subtract_numbers, divide_numbers, is_even, Calculator

# Test functions for add_numbers
def test_add_numbers_valid_inputs():
    assert add_numbers(2, 3) == 5
    assert add_numbers(10.5, 2.5) == 13.0
    assert add_numbers(-5, 5) == 0
    assert add_numbers(0,0) == 0

def test_add_numbers_invalid_inputs():
    with pytest.raises(TypeError):
        add_numbers("a", 2)
    with pytest.raises(TypeError):
        add_numbers(2, "b")
    with pytest.raises(TypeError):
        add_numbers("a", "b")


# Test functions for subtract_numbers
def test_subtract_numbers_valid_inputs():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(10.5, 2.5) == 8.0
    assert subtract_numbers(-5, 5) == -10
    assert subtract_numbers(0,0) == 0

def test_subtract_numbers_invalid_inputs():
    with pytest.raises(TypeError):
        subtract_numbers("a", 2)
    with pytest.raises(TypeError):
        subtract_numbers(2, "b")


# Test functions for divide_numbers
def test_divide_numbers_valid_inputs():
    assert divide_numbers(10, 2) == 5.0
    assert divide_numbers(10.5, 2.5) == 4.2
    assert divide_numbers(-10, 2) == -5.0

def test_divide_numbers_zero_division():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)
    with pytest.raises(ValueError):
        divide_numbers(0,0)

def test_divide_numbers_invalid_inputs():
    with pytest.raises(TypeError):
        divide_numbers("a", 2)
    with pytest.raises(TypeError):
        divide_numbers(2, "b")


# Test functions for is_even
def test_is_even_valid_inputs():
    assert is_even(2) == True
    assert is_even(0) == True
    assert is_even(-4) == True

def test_is_even_invalid_inputs():
    with pytest.raises(TypeError):
        is_even(2.5)
    with pytest.raises(TypeError):
        is_even("a")


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
    assert calc.calculate("divide", 10, 2) == 5.0
    assert calc.get_history() == ['10 divide 2 = 5.0']

def test_calculator_invalid_operation():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate("multiply", 2, 3)

def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate("divide", 10, 0)

def test_calculator_invalid_input_types():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.calculate("add", "a", 2)
    with pytest.raises(TypeError):
        calc.calculate("subtract", 2, "b")
    with pytest.raises(TypeError):
        calc.calculate("divide", "a", "b")


def test_calculator_history():
    calc = Calculator()
    calc.calculate("add", 1, 2)
    calc.calculate("subtract", 4,1)
    assert calc.get_history() == ['1 add 2 = 3', '4 subtract 1 = 3']

