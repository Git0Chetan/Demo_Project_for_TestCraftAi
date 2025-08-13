import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_8 import *


import pytest
from your_module import add_numbers, subtract_numbers, divide_numbers, is_even, Calculator  # Replace your_module


class TestMathFunctions:
    def test_add_numbers_valid(self):
        assert add_numbers(2, 3) == 5
        assert add_numbers(10.5, 2.5) == 13.0
        assert add_numbers(0, 0) == 0

    def test_add_numbers_invalid(self):
        with pytest.raises(TypeError):
            add_numbers("2", 3)
        with pytest.raises(TypeError):
            add_numbers(2, "3")
        with pytest.raises(TypeError):
            add_numbers("a", "b")

    def test_subtract_numbers_valid(self):
        assert subtract_numbers(5, 2) == 3
        assert subtract_numbers(10.5, 2.5) == 8.0
        assert subtract_numbers(0, 0) == 0

    def test_subtract_numbers_invalid(self):
        with pytest.raises(TypeError):
            subtract_numbers("5", 2)
        with pytest.raises(TypeError):
            subtract_numbers(5, "2")

    def test_divide_numbers_valid(self):
        assert divide_numbers(10, 2) == 5.0
        assert divide_numbers(10.5, 2.5) == 4.2
        assert divide_numbers(1,1) == 1.0

    def test_divide_numbers_invalid(self):
        with pytest.raises(ValueError):
            divide_numbers(10, 0)
        with pytest.raises(TypeError):
            divide_numbers("10", 2)
        with pytest.raises(TypeError):
            divide_numbers(10, "2")


    def test_is_even_valid(self):
        assert is_even(2) == True
        assert is_even(0) == True
        assert is_even(-2) == True

    def test_is_even_invalid(self):
        with pytest.raises(TypeError):
            is_even(2.5)
        with pytest.raises(TypeError):
            is_even("2")



class TestCalculator:
    def test_calculator_add(self):
        calc = Calculator()
        assert calc.calculate("add", 2, 3) == 5
        assert "2 add 3 = 5" in calc.get_history()

    def test_calculator_subtract(self):
        calc = Calculator()
        assert calc.calculate("subtract", 5, 2) == 3
        assert "5 subtract 2 = 3" in calc.get_history()

    def test_calculator_divide(self):
        calc = Calculator()
        assert calc.calculate("divide", 10, 2) == 5.0
        assert "10 divide 2 = 5.0" in calc.get_history()

    def test_calculator_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.calculate("divide", 10, 0)

    def test_calculator_invalid_operation(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.calculate("multiply", 2, 3) #Unsupported operation

    def test_calculator_invalid_input(self):
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.calculate("add", "2", 3)
        with pytest.raises(TypeError):
            calc.calculate("subtract", 5, "2")

    def test_calculator_history(self):
        calc = Calculator()
        calc.calculate("add", 2,3)
        calc.calculate("subtract",5,2)
        assert len(calc.get_history()) == 2
        assert "2 add 3 = 5" in calc.get_history()
        assert "5 subtract 2 = 3" in calc.get_history()

```

Remember to replace `"your_module"` with the actual name of the file containing your functions.  This improved version includes more comprehensive tests, particularly for edge cases and error handling.  It uses `pytest.raises` effectively to check for expected exceptions.  The `TestCalculator` class thoroughly exercises the `Calculator` class's functionality and history tracking.  This provides a robust test suite for your code.