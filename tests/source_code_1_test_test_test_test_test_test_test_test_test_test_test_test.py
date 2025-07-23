import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from source_code_1_test_test_test_test_test_test_test_test_test_test_test import *


import pytest
import sys

# Mock source_code_1.py for demonstration purposes
def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def divide_numbers(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def is_even(x):
    if isinstance(x, int):
        return x % 2 == 0
    else:
        raise TypeError("Input must be an integer")

class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, operation, x, y):
        if operation == "add":
            result = x + y
        elif operation == "subtract":
            result = x - y
        elif operation == "divide":
            if y == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = x / y
        elif operation == "multiply":
            result = x * y
        else:
            raise ValueError("Invalid operation")
        self.history.append(f"{x} {operation} {y} = {result}")
        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []


# Test cases for individual functions

def test_add_numbers_valid():
    assert add_numbers(2, 3) == 5
    assert add_numbers(2.5, 3.5) == 6.0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, 5) == 0
    assert add_numbers(100000, 100000) == 200000  # Test with large numbers

def test_add_numbers_invalid_type():
    with pytest.raises(TypeError):
        add_numbers("2", 3)
        add_numbers(2, "3")
        add_numbers("2", "3")
        add_numbers(2, [3])
        add_numbers(2, {'a': 3})


def test_subtract_numbers_valid():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(10.5, 2.5) == 8.0
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(-5, 5) == -10
    assert subtract_numbers(1000, 1) == 999  #Test with large numbers

def test_subtract_numbers_invalid_type():
    with pytest.raises(TypeError):
        subtract_numbers("5", 3)
        subtract_numbers(5, "3")
        subtract_numbers([5], 3)
        subtract_numbers(5, {'a': 3})


def test_divide_numbers_valid():
    assert divide_numbers(10, 2) == 5.0
    assert divide_numbers(10.5, 2.5) == 4.2
    assert divide_numbers(0, 5) == 0.0
    assert divide_numbers(1000, 10) == 100.0  # Test with large numbers
    assert divide_numbers(-10, 2) == -5.0  #Test with negative numbers


def test_divide_numbers_invalid():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)
    with pytest.raises(TypeError):
        divide_numbers("10", 2)
        divide_numbers(10, "2")
        divide_numbers([10], 2)
        divide_numbers(10, {'a': 2})



def test_is_even_valid():
    assert is_even(2) == True
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(100000) == True  #Test with large numbers


def test_is_even_invalid_type():
    with pytest.raises(TypeError):
        is_even(2.5)
        is_even("2")
        is_even([2])
        is_even({'a': 2})



# Test cases for Calculator class

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_calculator_add(self):
        assert self.calc.calculate("add", 2, 3) == 5
        assert self.calc.get_history() == ['2 add 3 = 5']

    def test_calculator_subtract(self):
        assert self.calc.calculate("subtract", 5, 2) == 3
        assert self.calc.get_history() == ['5 subtract 2 = 3']

    def test_calculator_divide(self):
        assert self.calc.calculate("divide", 10, 2) == 5.0
        assert self.calc.get_history() == ['10 divide 2 = 5.0']

    def test_calculator_multiply(self):
        assert self.calc.calculate("multiply", 5, 2) == 10
        assert self.calc.get_history() == ['5 multiply 2 = 10']

    def test_calculator_invalid_operation(self):
        with pytest.raises(ValueError):
            self.calc.calculate("invalid_op", 2, 3)

    def test_calculator_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.calculate("divide", 10, 0)

    def test_calculator_invalid_input_type(self):
        with pytest.raises(TypeError):
            self.calc.calculate("add", "2", 3)
            self.calc.calculate("add", 2, "3")
            self.calc.calculate("add", 2, [3])
            self.calc.calculate("add", [2], 3)


    def test_calculator_history_multiple_operations(self):
        self.calc.calculate("add", 2, 3)
        self.calc.calculate("subtract", 5, 2)
        self.calc.calculate("divide", 10, 2)
        assert self.calc.get_history() == ['2 add 3 = 5', '5 subtract 2 = 3', '10 divide 2 = 5.0']

    def test_calculator_clear_history(self):
        self.calc.calculate("add", 2, 3)
        self.calc.clear_history()
        assert self.calc.get_history() == []

    def test_calculator_edge_cases(self):
        assert self.calc.calculate("multiply", sys.maxsize, 0) == 0
        with pytest.raises(ZeroDivisionError):
            self.calc.calculate("divide", sys.maxsize, 0)

    def test_calculator_large_numbers(self):
        assert self.calc.calculate("add", 1000000000, 1000000000) == 2000000000
        assert self.calc.calculate("subtract", 1000000000, 500000000) == 500000000
        assert self.calc.calculate("multiply", 1000000, 1000) == 1000000000
        assert self.calc.calculate("divide", 1000000000, 1000) == 1000000.0

    def test_calculator_negative_numbers(self):
        assert self.calc.calculate("add", -5, 2) == -3
        assert self.calc.calculate("subtract", -5, 2) == -7
        assert self.calc.calculate("multiply", -5, 2) == -10
        assert self.calc.calculate("divide", -10, 2) == -5.0

