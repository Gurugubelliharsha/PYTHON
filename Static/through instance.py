#Define a static variable and access that through a instance 
class MyClass:
    static_var = input()

obj = MyClass()
print("Access through instance:", obj.static_var)