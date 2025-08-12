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

    def test_positive_multi_digit(self):
        assert is_armstrong_number(153) == True
        assert is_armstrong_number(370) == True
        assert is_armstrong_number(371) == True
        assert is_armstrong_number(407) == True

    def test_positive_large_number(self):
        assert is_armstrong_number(1634) == True #A larger Armstrong number.
        assert is_armstrong_number(8208) == True #Another larger one.
        assert is_armstrong_number(9474) == True # And another.

    def test_negative_number(self):
        assert is_armstrong_number(-153) == False  #Negative numbers are not Armstrong

    def test_zero(self):
        assert is_armstrong_number(0) == True #Zero is considered an Armstrong number

    def test_non_armstrong_number(self):
        assert is_armstrong_number(123) == False
        assert is_armstrong_number(999) == False
        assert is_armstrong_number(1000) == False


    def test_large_non_armstrong(self):
        assert is_armstrong_number(10000) == False #testing a large number that is not an armstrong number.


    def test_string_input(self):
        with pytest.raises(TypeError):
            is_armstrong_number("153") #Test for invalid input type


    def test_float_input(self):
        with pytest.raises(TypeError):
            is_armstrong_number(153.5)

    def test_special_characters(self):
        with pytest.raises(TypeError): #Test for special characters as input.
            is_armstrong_number("abc")
        with pytest.raises(TypeError):
            is_armstrong_number("1a")


