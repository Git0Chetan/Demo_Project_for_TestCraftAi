import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Source_code_4 import *


import pytest
from your_module import is_prime  # Replace your_module with the actual module name

class TestIsPrime:
    """Comprehensive test suite for the is_prime function."""

    def test_prime_numbers(self):
        """Test with known prime numbers."""
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
        assert is_prime(11) == True
        assert is_prime(97) == True
        assert is_prime(101) == True


    def test_non_prime_numbers(self):
        """Test with known non-prime numbers."""
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
        assert is_prime(10) == False
        assert is_prime(100) == False
        assert is_prime(1000) == False


    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        assert is_prime(0) == False
        assert is_prime(-1) == False
        assert is_prime(-10) == False
        assert is_prime(2) == True # repeated for emphasis
        assert is_prime(3) == True # repeated for emphasis


    def test_large_prime_numbers(self):
        """Test with some large prime numbers."""
        assert is_prime(104729) == True  # A fairly large prime
        assert is_prime(104743) == True # Another large prime


    def test_large_non_prime_numbers(self):
        """Test with some large non-prime numbers."""
        assert is_prime(104730) == False # even number
        assert is_prime(104744) == False # divisible by 2


    def test_zero_input(self):
      with pytest.raises(TypeError): #This test should not raise an error if the function handles 0 correctly
          is_prime(0)

    def test_negative_input(self):
      with pytest.raises(TypeError): #This test should not raise an error if the function handles negative numbers correctly.
          is_prime(-5)

    def test_string_input(self):
        with pytest.raises(TypeError):
            is_prime("ten")

    def test_float_input(self):
        with pytest.raises(TypeError):
            is_prime(3.14)



```

**To run this test suite:**

1.  **Save:** Save the code above as a file named `test_is_prime.py` (or a similar descriptive name).  Make sure the `is_prime` function is in a file called `your_module.py` (replace `your_module` with your actual file name) in the same directory.

2.  **Install pytest:** If you don't have pytest installed, open your terminal or command prompt and run:  `pip install pytest`

3.  **Run pytest:** Navigate to the directory containing `test_is_prime.py` and run: `pytest`

Pytest will automatically discover and run the tests, providing a summary of successes and failures.  The error handling tests (`test_zero_input`, `test_negative_input`, `test_string_input`, `test_float_input`) specifically check for appropriate error handling behavior. If `is_prime` is properly written to handle these, the assertions should not raise exceptions. If the function does not handle them correctly (e.g., it crashes when given a string) the `with pytest.raises(...)` block will catch the expected error and the test will pass.  If the function *doesn't* raise an exception when it should, the test will fail.