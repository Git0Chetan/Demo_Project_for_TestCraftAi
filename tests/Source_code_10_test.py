import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_10 import *


def test_your_function_valid_input(): # Replace your_function with the actual function name
    assert your_function(1) == 2 # Replace with appropriate assertion

def test_your_function_invalid_input():
    with pytest.raises(TypeError):
        your_function("a")

def test_your_function_edge_case():
    assert your_function(0) == 1

# Add more test functions for other functions in your module


@pytest.fixture
def your_class_instance(): # Replace your_class with the actual class name
    return YourClass() # Replace YourClass with the actual class name


def test_your_class_init(your_class_instance):
    assert isinstance(your_class_instance, YourClass)

def test_your_class_method_valid_input(your_class_instance): #Replace your_class_method with the actual method name
    assert your_class_instance.your_class_method(1) == 2 # Replace with appropriate assertion

def test_your_class_method_invalid_input(your_class_instance):
    with pytest.raises(ValueError):
        your_class_instance.your_class_method(-1)

@pytest.mark.parametrize("test_input, expected", [(1,2), (2,4), (3,6)])
def test_your_function_parametrized(test_input, expected):
    assert your_function(test_input) == expected

# Add more test functions for other class methods and edge cases


def test_error_condition():
    with pytest.raises(Exception): # Replace Exception with the specific exception
        your_function(-1) # Replace with the function call that raises the exception

