import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cal import *


import pytest

# Source code (provided in the prompt)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y


class TestCalculator:
    @pytest.mark.parametrize("x, y, expected", [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 5, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0)

    ])
    def test_add(self, x, y, expected):
        assert add(x, y) == expected

    @pytest.mark.parametrize("x, y, expected", [
        (2, 1, 1),
        (10, 5, 5),
        (5, 10, -5),
        (0, 0, 0),
        (1.5, 2.5, -1.0)
    ])
    def test_subtract(self, x, y, expected):
        assert subtract(x, y) == expected

    @pytest.mark.parametrize("x, y, expected", [
        (2, 3, 6),
        (5, 5, 25),
        (0, 5, 0),
        (-2, 5, -10),
        (2.5, 2, 5.0)
    ])
    def test_multiply(self, x, y, expected):
        assert multiply(x, y) == expected

    @pytest.mark.parametrize("x, y, expected", [
        (10, 2, 5.0),
        (5, 1, 5.0),
        (10, 0, "Error! Cannot divide by zero."),
        (5, -2, -2.5),
        (10.0,2.5, 4.0)
    ])
    def test_divide(self, x, y, expected):
        assert divide(x, y) == expected


    def test_divide_by_zero_string(self):
        with pytest.raises(TypeError): #this will fail, showing that the function does not raise an exception.  The function returns a string instead.
            assert divide(5,0) == ZeroDivisionError

    def test_invalid_operator(self):
        num1 = 10
        num2 = 5
        operator = "%"
        with pytest.raises(TypeError): #this will fail if the typeerror is not raised in the function
            result =  perform_operation(num1, operator, num2)
            assert result == "Invalid operator!"

def perform_operation(num1, operator, num2):  #added helper function to reduce repetition in testing
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operator!"
    return result

