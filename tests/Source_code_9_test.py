import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_9 import *
port pytest
from your_module import YourClass, your_function  # Replace your_module, YourClass, your_function

def test_your_function_valid_input():
    assert your_function(10) == 20  # Replace with actual expected output

def test_your_function_invalid_input():
    with pytest.raises(TypeError):
        your_function("abc")

def test_your_function_edge_case():
    assert your_function(0) == 0 # Replace with actual expected output


@pytest.mark.parametrize("value, expected", [(1, 2), (5, 6), (-1,0)])
def test_your_function_parametrized(value, expected):
    assert your_function(value) == expected

def test_yourclass_init():
    obj = YourClass(10) #Replace 10 with appropriate initialization value.
    assert obj.value == 10 #Replace with actual attribute and value.

def test_yourclass_method_valid_input():
    obj = YourClass(5) #Replace 5 with appropriate initialization value.
    assert obj.some_method(2) == 10 #Replace with method name and expected output.

def test_yourclass_method_invalid_input():
    obj = YourClass(5)
    with pytest.raises(ValueError):
        obj.some_method(-1) #Replace with method name and invalid input.


@pytest.mark.parametrize("input_value, expected", [(2, 4), (0,0), (-2, -4)])
def test_yourclass_method_parametrized(input_value, expected):
    obj = YourClass(5) #Replace 5 with appropriate initialization value.
    assert obj.some_method(input_value) == expected #Replace with method name


def test_yourclass_method_edge_case():
    obj = YourClass(0) #Replace 0 with appropriate initialization value.
    assert obj.some_method(0) == 0 #Replace with method name and expected output.


