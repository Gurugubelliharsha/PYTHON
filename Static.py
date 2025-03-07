#Define a static variable and access that through a class  
class MyClass:
    static_var = input()

print("Access through class:", MyClass.static_var)


#Define a static variable and access that through a instance 
class MyClass:
    static_var = input()

obj = MyClass()
print("Access through instance:", obj.static_var)

#Define a static variable and change within the class
class MyClass:
    static_var = input("Enter static variable: ")
print("Before change:", MyClass.static_var)
MyClass.static_var = input("Enter new value for class: ")
print("After change:", MyClass.static_var)

#Define a static variable and change within the instance
class MyClass:
    static_var = input("Enter static variable: ")

obj = MyClass()
obj.static_var = input("Enter new value for instance: ")

print("Class static variable:", MyClass.static_var)
print("Instance variable after change:", obj.static_var)