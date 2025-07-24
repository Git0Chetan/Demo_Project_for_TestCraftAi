import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Fibonacii import *


import pytest
from temp import fibonacci  # Assuming the fibonacci function is in a file named temp.py

class TestFibonacci:
    def test_fibonacci_zero_terms(self):
        assert fibonacci(0) == []

    def test_fibonacci_one_term(self):
        assert fibonacci(1) == [0]

    def test_fibonacci_two_terms(self):
        assert fibonacci(2) == [0, 1]

    def test_fibonacci_positive_terms(self):
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_large_number_of_terms(self):
        assert fibonacci(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]


    def test_fibonacci_negative_terms(self):
        with pytest.raises(ValueError):  # Expecting ValueError or similar for negative input.  Adjust as needed based on your fibonacci function's error handling.
            fibonacci(-5)

    def test_fibonacci_non_integer_input(self):
        with pytest.raises(TypeError): # Expecting TypeError if input is not an integer. Adjust as needed.
            fibonacci(3.14)
        with pytest.raises(TypeError):
            fibonacci("abc")


    def test_fibonacci_very_large_number(self):
        #Test for potential overflow or performance issues with very large numbers. Adjust as needed for your system's limits.
        #This test might take a while depending on your system. Consider using a smaller number or a more sophisticated performance test.
        result = fibonacci(100)
        assert len(result) == 100 # Check length at least, more robust checks might be needed depending on the potential issues.

```

To run this test suite, save the code above as a file (e.g., `test_fibonacci.py`) and  make sure you have `pytest` installed (`pip install pytest`). Then, navigate to the directory containing the file in your terminal and run:

```bash
pytest test_fibonacci.py
```

pytest will automatically discover and run the test functions.  The output will show you which tests passed and which failed, along with any error messages.  Remember to adjust the error handling assertions (e.g., `pytest.raises`) if your `fibonacci` function throws different exceptions than what's expected.  For extremely large numbers in `test_fibonacci_very_large_number`, you may want a less strict assertion, focusing on the length of the sequence instead of the values themselves to prevent extremely long run times.