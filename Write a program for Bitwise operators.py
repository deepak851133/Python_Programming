#Q3: Write a program for Bitwise operators.
# Accept two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Bitwise operations
bitwise_and = num1 & num2  # AND
bitwise_or = num1 | num2   # OR
bitwise_xor = num1 ^ num2  # XOR
bitwise_not = ~num1       # NOT (inverts all bits of num1)
bitwise_left_shift = num1 << 2  # Left shift num1 by 2 positions
bitwise_right_shift = num1 >> 2  # Right shift num1 by 2 positions

# Display the results
print(f"Bitwise AND: {num1} & {num2} = {bitwise_and}")
print(f"Bitwise OR: {num1} | {num2} = {bitwise_or}")
print(f"Bitwise XOR: {num1} ^ {num2} = {bitwise_xor}")
print(f"Bitwise NOT: ~{num1} = {bitwise_not}")
print(f"Bitwise Left Shift: {num1} << 2 = {bitwise_left_shift}")
print(f"Bitwise Right Shift: {num1} >> 2 = {bitwise_right_shift}")
