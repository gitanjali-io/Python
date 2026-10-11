# input two variables 
a=int(input("Enter a value of the first variable :"))
b=int(input("Enter a value of the second variable :"))
print("Before swapping ")
print("The value of a is :", a)
print("The value of b is :", b)
temp = a 
a = b 
b = temp 
print("After swapping ")
print("The value of a is :", a)
print("The value of b is :", b)