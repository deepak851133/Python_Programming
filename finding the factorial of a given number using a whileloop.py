#3.Write a python program finding the factorial of a given number using a whileloop
# Accept a number from the user
number = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Use a while loop to calculate the factorial
while number > 0:
    factorial *= number  # Multiply current number with factorial
    number -= 1  # Decrease number by 1

# Display the result
print(f"The factorial is: {factorial}")
