import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_12 import *



def test_compound_interest_positive_values():
    assert compound_interest(10000, 10.25, 5) == pytest.approx(6288.946267774414)

def test_compound_interest_zero_principal():
    assert compound_interest(0, 10.25, 5) == 0.0

def test_compound_interest_zero_rate():
    assert compound_interest(10000, 0, 5) == 0.0

def test_compound_interest_zero_time():
    assert compound_interest(10000, 10.25, 0) == 0.0

def test_compound_interest_negative_principal():
    with pytest.raises(ValueError):
        compound_interest(-10000, 10.25, 5)

def test_compound_interest_negative_rate():
    with pytest.raises(ValueError):
        compound_interest(10000, -10.25, 5)

def test_compound_interest_negative_time():
    with pytest.raises(ValueError):
        compound_interest(10000, 10.25, -5)

def test_compound_interest_large_numbers():
    assert compound_interest(1000000, 15, 20) == pytest.approx(16366537.7049)

def test_compound_interest_decimal_values():
    assert compound_interest(1234.56, 7.89, 3.5) == pytest.approx(372.6617)

def test_compound_interest_invalid_input_type():
    with pytest.raises(TypeError):
        compound_interest("abc", 10.25, 5)
    with pytest.raises(TypeError):
        compound_interest(10000, "abc", 5)
    with pytest.raises(TypeError):
        compound_interest(10000, 10.25, "abc")
