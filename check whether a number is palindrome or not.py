#2.Write a python program to check whether a number is palindrome or not?
# Accept a number from the user
number = int(input("Enter a number: "))

# Store the original number
original_number = number

# Reverse the number
reversed_number = 0
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number = number // 10  # Remove the last digit from the number

# Check if the original number is equal to the reversed number
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
