#Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.  
#Also, Access the PROTECTED fields and methods from child class located in a different package 
#Access the PROTECTED fields and methods from any class in different package 
class Parent:
    def __init__(self):
        self._protected_var = "I am Protected"
    def _protected_method(self):
        print("Protected Method Inside Parent")
class SamePackage:
    def access_protected(self):
        obj = Parent()
        print("Accessing Protected Variable:", obj._protected_var)
        obj._protected_method()
class Child(Parent):
    def child_method(self):
        print("Accessing Protected Variable in Subclass:", self._protected_var)
        self._protected_method()
if __name__ == "__main__":
    obj1 = SamePackage()
    obj1.access_protected()
    obj2 = Child()
    obj2.child_method()