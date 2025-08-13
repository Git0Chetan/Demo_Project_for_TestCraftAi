import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_9 import *


import pytest
from example import *

def test_calculate_average_valid():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_empty():
    assert calculate_average([]) == 0.0

def test_calculate_average_negative():
    assert calculate_average([-1, -2, -3]) == -2.0

def test_calculate_average_mixed():
    assert calculate_average([1, -2, 3, -4, 5]) == 0.6

def test_calculate_average_zero():
    assert calculate_average([0,0,0]) == 0.0


def test_MyClass_init():
    obj = MyClass("test")
    assert obj.name == "test"

def test_MyClass_init_empty():
    obj = MyClass("")
    assert obj.name == ""

def test_MyClass_init_numeric():
    with pytest.raises(TypeError):
        MyClass(123)

def test_MyClass_greet_valid():
    obj = MyClass("test")
    assert obj.greet() == "Hello, test!"

def test_MyClass_greet_empty():
    obj = MyClass("")
    assert obj.greet() == "Hello, !"

def test_process_data_valid():
    assert process_data([1,2,3]) == [2,3,4]

def test_process_data_empty():
    assert process_data([]) == []

def test_process_data_negative():
    assert process_data([-1,-2,-3]) == [0,-1,-2]

def test_process_data_mixed():
    assert process_data([1,-2,3]) == [2,1,4]

def test_process_data_strings():
    with pytest.raises(TypeError):
        process_data(["a","b","c"])

