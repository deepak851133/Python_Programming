#Q4: Write a program to calculate greatest of three numbers. 
 
a= int(input("Enter 1st number: ")) 
b= int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: ")) 
 
if a > b and a > c: 
    print("a is the greatest number") 
elif b > c:
    print("b is the greatest number")
else:
    print("c is the greatest number") 
