#Define the local and Global variables with the same name and print both variables and understand the scope of the variables
x = "Global Variable"
def my_fun():
    x = "Local Variable"
    print("Inside function:", x)
my_fun()
print("Outside function:", x) 