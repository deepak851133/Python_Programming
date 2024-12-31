#1.Write a python program to reverse a number using a while loop.
# Accept a number from the user
number = int(input("Enter a number: "))

# Initialize the reversed number to 0
reversed_number = 0

# Use a while loop to reverse the number
while number > 0:
    digit = number % 10  # Get the last digit
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number = number // 10  # Remove the last digit from the number

# Display the reversed number
print(f"The reversed number is: {reversed_number}")
