#2.Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number
# Define the square function
def square(number):
    # Calculate and return the square of the number
    return number ** 2

# Call the function with a number
num = float(input("Enter a number: "))
result = square(num)

# Display the result
print(f"The square of {num} is {result}.")
