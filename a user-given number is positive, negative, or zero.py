#4.Create a Python program that checks if a user-given number is positive, negative, or zero
# Taking input from the user
number = float(input("Enter a number: "))

# Checking if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
