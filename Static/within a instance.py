#Define a static variable and change within the instance
class MyClass:
    static_var = input("Enter static variable: ")

obj = MyClass()
obj.static_var = input("Enter new value for instance: ")

print("Class static variable:", MyClass.static_var)
print("Instance variable after change:", obj.static_var)