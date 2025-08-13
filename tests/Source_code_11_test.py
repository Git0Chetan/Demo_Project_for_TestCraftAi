import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_11 import *

from your_module import YourClass, your_function

@pytest.fixture
def your_class_instance():
    return YourClass()

def test_your_class_init():
    instance = YourClass()
    assert isinstance(instance, YourClass)

@pytest.mark.parametrize("arg1, expected", [
    (1, 2),
    (0, 1),
    (-1, 0),
    (10, 11),
])
def test_your_class_method(your_class_instance, arg1, expected):
    result = your_class_instance.your_method(arg1)
    assert result == expected

@pytest.mark.parametrize("arg1, arg2, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (0, 'a', pytest.raises(TypeError)),
])
def test_your_class_another_method(your_class_instance, arg1, arg2, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            your_class_instance.another_method(arg1, arg2)
    else:
        result = your_class_instance.another_method(arg1, arg2)
        assert result == expected


@pytest.mark.parametrize("arg, expected", [
    (1, 2),
    (0, 1),
    (-1, 0),
    (10, 11),
    ("a", pytest.raises(TypeError)),
    (1.5, 2.5),
])
def test_your_function(arg, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            your_function(arg)
    else:
        result = your_function(arg)
        assert result == expected
