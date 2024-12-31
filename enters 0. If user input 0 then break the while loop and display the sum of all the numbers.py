#4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
# Initialize the sum variable
total_sum = 0

# Start an infinite while loop
while True:
    # Accept a number from the user
    number = int(input("Enter a number (enter 0 to stop): "))
    
    # If the user enters 0, break the loop
    if number == 0:
        break
    
    # Add the number to the total sum
    total_sum += number

# Display the total sum
print(f"The sum of all the numbers is: {total_sum}")
