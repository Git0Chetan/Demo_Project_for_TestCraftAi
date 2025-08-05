def is_armstrong_number(n):
    """Check if a number is an Armstrong number."""
    # Convert number to string to get its digits
    num_str = str(n)
    length = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** length
    
    return total == n

# Input from user
number = int(input("Enter a number: "))

# Check and display
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
