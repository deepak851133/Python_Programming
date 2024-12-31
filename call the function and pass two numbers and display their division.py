#1.Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
# Define the div function
def div(a, b):
    # Perform division and return the result
    return a / b

# Call the function with two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number is not zero
if num2 != 0:
    result = div(num1, num2)
    print(f"The division of {num1} by {num2} is {result}.")
else:
    print("Division by zero is not allowed.")
