#2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
# Taking age as input from the user
age = int(input("Enter your age: "))

# Checking voting eligibility
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
