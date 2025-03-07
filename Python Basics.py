#Write a program to print your name. 
print("Harsha")

#Write a program for a Single line comment and multi-line comments 

# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
Used to describe the code in detail.
"""
print("Above are the Comments in Python")


#Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 
a = 10        # Integer
b = True      # Boolean
c = 'A'       # Character
d = 10.5      # Float
e = 20.123456789  # Double

print("Integer: ", a)
print("Boolean: ", b)
print("Character: ", c)
print("Float: ", d)
print("Double: ", e)

#Define the local and Global variables with the same name and print both variables and understand the scope of the variables
x = "Global Variable"
def my_fun():
    x = "Local Variable"
    print("Inside function:", x)
my_fun()
print("Outside function:", x) 