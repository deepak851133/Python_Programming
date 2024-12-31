#3.Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated numbers
print("The random numbers are:", numbers)

# Find and display the maximum and minimum
maximum = max(numbers)
minimum = min(numbers)

print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")
