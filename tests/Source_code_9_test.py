import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_9 import *


import pytest
from your_module import calculate_average, process_data, MyClass  # Replace your_module

def test_calculate_average_empty_list():
    with pytest.raises(ZeroDivisionError):
        calculate_average([])

def test_calculate_average_single_element():
    assert calculate_average([5]) == 5

def test_calculate_average_multiple_elements():
    assert calculate_average([1, 2, 3, 4, 5]) == 3

def test_calculate_average_negative_numbers():
    assert calculate_average([-1, 0, 1]) == 0

def test_calculate_average_mixed_numbers():
    assert calculate_average([-2, 0, 2, 4]) == 1


@pytest.mark.parametrize("input_data, expected_output", [
    ([1, 2, 3], [2, 3, 4]),
    ([-1, 0, 1], [0, 1, 2]),
    ([5], [6]),
    ([], []),
])
def test_process_data(input_data, expected_output):
    assert process_data(input_data) == expected_output


def test_MyClass_init():
    obj = MyClass(10)
    assert obj.value == 10

def test_MyClass_init_invalid():
    with pytest.raises(TypeError):
        MyClass("abc")

def test_MyClass_method1():
    obj = MyClass(5)
    assert obj.method1() == 10

def test_MyClass_method2():
    obj = MyClass(5)
    assert obj.method2(2) == 7

@pytest.mark.parametrize("input_value, expected_result", [
    (5, 10),
    (0, 0),
    (-5, 0),
    (10.5, 21),
])
def test_MyClass_method1_param(input_value, expected_result):
    obj = MyClass(input_value)
    assert obj.method1() == expected_result

@pytest.mark.parametrize("input_value, input_add, expected_result", [
    (5, 2, 7),
    (0, 10, 10),
    (-5, 5, 0),
    (10.5, 2, 12.5),
])
def test_MyClass_method2_param(input_value, input_add, expected_result):
    obj = MyClass(input_value)
    assert obj.method2(input_add) == expected_result

