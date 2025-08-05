import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_5 import *


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
    @pytest.mark.parametrize("input_number, expected_result", [
        (0, True),  #Edge case: Zero
        (1, True),  #Edge case: single digit
        (153, True),  #Example Armstrong Number
        (370, True),  #Example Armstrong Number
        (371, True),  #Example Armstrong Number
        (407, True),  #Example Armstrong Number
        (1634, True), #Example Armstrong Number
        (9474, True), #Example Armstrong Number
        (54748, True),#Example Armstrong Number
        (92727, True),#Example Armstrong Number
        (93084, True),#Example Armstrong Number
        (54748, True),#Example Armstrong Number
        (1, True),
        (10, False),
        (100, False),
        (152, False),
        (371,True),
        (1000, False), #Example Non-Armstrong Number
        (9999, False), #Example Non-Armstrong Number
        (-1, False), #Negative Number
        (123456789, False), #Large Number
        (12345678901234567890, False) #Very Large Number
    ])
    def test_is_armstrong_number(self, input_number, expected_result):
        assert is_armstrong_number(input_number) == expected_result


    def test_zero_input():
        assert is_armstrong_number(0) == True

    def test_negative_input():
        with pytest.raises(Exception) as e: #expecting no specific error, just that an error is raised
            is_armstrong_number(-153) #expecting no specific error, just that an error is raised
    
    def test_large_number():
        assert is_armstrong_number(123456789) == False

    def test_string_input():
        with pytest.raises(TypeError):
            is_armstrong_number("153")

    def test_float_input():
        with pytest.raises(TypeError):
            is_armstrong_number(153.5)

    def test_invalid_input():
        with pytest.raises(TypeError):
            is_armstrong_number([1, 5, 3]) #testing against an array

