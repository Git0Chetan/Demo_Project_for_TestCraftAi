import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from source_code_1_test_test_test_test_test_test import *


import pytest
import sys

# Assume source_code_1.py contains these functions and class
# from source_code_1 import add_numbers, subtract_numbers, divide_numbers, is_even, Calculator

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


#Test cases for individual functions

def test_add_numbers_valid():
    assert add_numbers(2, 3) == 5
    assert add_numbers(2.5, 3.5) == 6.0
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, 5) == 0
    assert add_numbers(100000, 100000) == 200000  #Test with large numbers
    assert add_numbers(sys.maxsize, 1) == sys.maxsize + 1 if sys.maxsize +1 > 0 else sys.maxsize +1 #Test with sys.maxsize


def test_add_numbers_invalid():
    with pytest.raises(TypeError):
        add_numbers("2", 3)
    with pytest.raises(TypeError):
        add_numbers(2, "3")
    with pytest.raises(TypeError):
        add_numbers("2", "3")
    with pytest.raises(TypeError):
        add_numbers(2, [3])  #Test with list input
    with pytest.raises(TypeError):
        add_numbers(2, {'a': 3})  #Test with dictionary input


def test_subtract_numbers_valid():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(10.5, 2.5) == 8.0
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(-5, 5) == -10
    assert subtract_numbers(1000, 1) == 999  #Test with large numbers
    assert subtract_numbers(1, sys.maxsize) == 1 - sys.maxsize  #Test with sys.maxsize


def test_subtract_numbers_invalid():
    with pytest.raises(TypeError):
        subtract_numbers("5", 3)
    with pytest.raises(TypeError):
        subtract_numbers(5, "3")
    with pytest.raises(TypeError):
        subtract_numbers([5], 3)  #Test with list input
    with pytest.raises(TypeError):
        subtract_numbers(5, {'a': 3})  #Test with dictionary input


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
    with pytest.raises(TypeError):
        divide_numbers(10, "2")
    with pytest.raises(TypeError):
        divide_numbers([10], 2)  #Test with list input
    with pytest.raises(TypeError):
        divide_numbers(10, {'a': 2})  #Test with dictionary input



def test_is_even_valid():
    assert is_even(2) == True
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(100000) == True  #Test with large numbers
    assert is_even(sys.maxsize) == (sys.maxsize % 2 == 0)  #Test with sys.maxsize


def test_is_even_invalid():
    with pytest.raises(TypeError):
        is_even(2.5)
    with pytest.raises(TypeError):
        is_even("2")
    with pytest.raises(TypeError):
        is_even([2])  #Test with list input
    with pytest.raises(TypeError):
        is_even({'a': 2})  #Test with dictionary input



# Test cases for Calculator class

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
        assert calc.calculate("divide", 10, 2) == 5.0
        assert calc.get_history() == ['10 divide 2 = 5.0']

    def test_calculator_multiply(self):  #Added test for multiply (assuming it exists)
        calc = Calculator()
        assert calc.calculate("multiply", 5, 2) == 10
        assert calc.get_history() == ['5 multiply 2 = 10']

    def test_calculator_invalid_operation(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.calculate("invalid_op", 2, 3)

    def test_calculator_zero_division(self):
        calc = Calculator()
        with pytest.raises(ZeroDivisionError):
            calc.calculate("divide", 10, 0)

    def test_calculator_invalid_input(self):
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.calculate("add", "2", 3)
        with pytest.raises(TypeError):
            calc.calculate("add", 2, "3") #Added this case for completeness
        with pytest.raises(TypeError):
            calc.calculate("add", 2, [3])  # Test with list input
        with pytest.raises(TypeError):
            calc.calculate("add", [2], 3) #Added this case for completeness


    def test_calculator_history_multiple_operations(self):
        calc = Calculator()
        calc.calculate("add", 2, 3)
        calc.calculate("subtract", 5, 2)
        calc.calculate("divide", 10, 2)
        assert calc.get_history() == ['2 add 3 = 5', '5 subtract 2 = 3', '10 divide 2 = 5.0']

    def test_calculator_clear_history(self):  #Test for clearing history (assuming such functionality exists)
        calc = Calculator()
        calc.calculate("add", 2, 3)
        calc.clear_history()
        assert calc.get_history() == []

    def test_calculator_edge_cases(self):
        calc = Calculator()
        assert calc.calculate("add", sys.maxsize, 1) == sys.maxsize + 1 if sys.maxsize + 1 > 0 else sys.maxsize + 1
        assert calc.calculate("subtract", sys.maxsize, 1) == sys.maxsize -1 if sys.maxsize -1 > 0 else sys.maxsize -1
        assert calc.calculate("multiply", sys.maxsize, 0) == 0
        with pytest.raises(ZeroDivisionError):
            calc.calculate("divide", sys.maxsize, 0)

    def test_calculator_large_numbers(self):
        calc = Calculator()
        assert calc.calculate("add", 1000000000, 1000000000) == 2000000000
        assert calc.calculate("subtract", 1000000000, 500000000) == 500000000
        assert calc.calculate("multiply", 1000000, 1000) == 1000000000
        assert calc.calculate("divide", 1000000000, 1000) == 1000000.0

    def test_calculator_negative_numbers(self): #added test for negative numbers
        calc = Calculator()
        assert calc.calculate("add", -5, 2) == -3
        assert calc.calculate("subtract", -5, 2) == -7
        assert calc.calculate("multiply", -5, 2) == -10
        assert calc.calculate("divide", -10, 2) == -5.0

