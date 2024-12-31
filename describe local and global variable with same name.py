#Q4. write a code that describe local and global variable with same name ?
# Global variable
x = "Global Variable"

def my_function():
    # Local variable with the same name as the global variable
    x = "Local Variable"
    print("Inside the function, x =", x)  # Refers to the local variable

# Call the function
my_function()

# Outside the function, x refers to the global variable
print("Outside the function, x =", x)
