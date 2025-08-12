import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_6 import *


import pytest

def is_armstrong_number(n):
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    length = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** length
    return total == n

class TestArmstrongNumber:
    def test_positive_single_digit(self):
        assert is_armstrong_number(5) == True
        assert is_armstrong_number(1) == True

    def test_positive_multi_digit(self):
        assert is_armstrong_number(153) == True
        assert is_armstrong_number(370) == True
        assert is_armstrong_number(371) == True
        assert is_armstrong_number(407) == True
        assert is_armstrong_number(1634) == True #A larger Armstrong number

    def test_positive_not_armstrong(self):
        assert is_armstrong_number(100) == False
        assert is_armstrong_number(200) == False
        assert is_armstrong_number(999) == False
        assert is_armstrong_number(123) == False

    def test_zero(self):
        assert is_armstrong_number(0) == True #0 is considered an Armstrong number

    def test_negative_numbers(self):
        with pytest.raises(Exception) as e: #This test will raise an error because the logic doesn't handle negative numbers gracefully
            is_armstrong_number(-1)


    def test_large_number(self):
        # Armstrong numbers get exceedingly rare as they grow larger,  this tests the function with a large non-Armstrong number
        assert is_armstrong_number(99999999999999999999999999999999) == False

    def test_string_input(self):
        with pytest.raises(TypeError) as e:
            is_armstrong_number("153")
        assert str(e.value) == "must be int, not str" #The specific error message depends on how the function internally converts the input to a string

    def test_float_input(self):
        with pytest.raises(TypeError) as e:
            is_armstrong_number(153.0)
        assert str(e.value) == "must be int, not float" #The specific error message depends on how the function internally converts the input to a string

    def test_special_characters(self):
        with pytest.raises(TypeError) as e:
            is_armstrong_number("1a53")
        assert "invalid literal for int() with base 10" in str(e.value) #This error message is specific to the invalid input given to `int()`


