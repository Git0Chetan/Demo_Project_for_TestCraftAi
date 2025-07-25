# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
num_terms = 10 
print(f"Fibonacci series with {num_terms} terms:")
print(fibonacci(num_terms))
