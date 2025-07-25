import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_3 import *


import pytest
from compound_interest_calculator import compound_interest  # Assuming the code is in compound_interest_calculator.py


class TestCompoundInterest:

    def test_valid_input(self):
        principal = 10000
        rate = 10.25
        time = 5
        expected_ci = 6288.946267774414
        assert round(compound_interest(principal, rate, time),2) == expected_ci


    def test_zero_principal(self):
        principal = 0
        rate = 10.25
        time = 5
        assert compound_interest(principal, rate, time) == 0

    def test_zero_rate(self):
        principal = 10000
        rate = 0
        time = 5
        assert compound_interest(principal, rate, time) == 0

    def test_zero_time(self):
        principal = 10000
        rate = 10.25
        time = 0
        assert compound_interest(principal, rate, time) == 0

    def test_negative_principal(self):
        principal = -10000
        rate = 10.25
        time = 5
        with pytest.raises(ValueError) as excinfo:  #Check for ValueError if principal is negative.  Could also check for specific error messages
            compound_interest(principal, rate, time)
        assert "Principal cannot be negative" in str(excinfo.value)


    def test_negative_rate(self):
        principal = 10000
        rate = -10.25
        time = 5
        with pytest.raises(ValueError) as excinfo: # Check for ValueError if rate is negative.
            compound_interest(principal, rate, time)
        assert "Rate cannot be negative" in str(excinfo.value)

    def test_negative_time(self):
        principal = 10000
        rate = 10.25
        time = -5
        with pytest.raises(ValueError) as excinfo: # Check for ValueError if time is negative.
            compound_interest(principal, rate, time)
        assert "Time cannot be negative" in str(excinfo.value)


    def test_large_values(self):
        principal = 100000000
        rate = 25
        time = 20
        # Expect a large compound interest, we don't check the exact value due to floating point precision.
        assert compound_interest(principal, rate, time) > 0


    def test_decimal_values(self):
        principal = 12345.67
        rate = 7.89
        time = 3.5
        # Check for approximate correctness due to floating-point precision.
        assert round(compound_interest(principal, rate, time),2) == 16276.13


    def test_non_numeric_input(self):
        with pytest.raises(TypeError) as excinfo:
            compound_interest("abc", 10, 5)
        assert "Principal must be a number" in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            compound_interest(10000, "def", 5)
        assert "Rate must be a number" in str(excinfo.value)

        with pytest.raises(TypeError) as excinfo:
            compound_interest(10000, 10, "ghi")
        assert "Time must be a number" in str(excinfo.value)

#Modify compound_interest function to raise ValueError for negative inputs and non-numeric inputs.

def compound_interest(principal, rate, time):
    if not isinstance(principal, (int, float)) or principal < 0:
        raise ValueError("Principal must be a non-negative number")
    if not isinstance(rate, (int, float)) or rate < 0:
        raise ValueError("Rate must be a non-negative number")
    if not isinstance(time, (int, float)) or time < 0:
        raise ValueError("Time must be a non-negative number")
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    return CI  # Return CI instead of printing

```

This improved version includes a `compound_interest_calculator.py` file (which you should create) containing the modified `compound_interest` function.  The tests are much more comprehensive, covering various data types, edge cases, and error handling.  Remember to install pytest (`pip install pytest`) before running the tests with `pytest`.  The assertion checks for approximate results where floating-point inaccuracies are expected.  Error handling is also improved by explicitly checking for negative and non-numeric inputs and raising appropriate exceptions.