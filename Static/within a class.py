#Define a static variable and change within the class
class MyClass:
    static_var = input("Enter static variable: ")
print("Before change:", MyClass.static_var)
MyClass.static_var = input("Enter new value for class: ")
print("After change:", MyClass.static_var)