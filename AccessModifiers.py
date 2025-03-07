#Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method. 
#Create a sub class and try to access the private fields and methods from sub class.
class Parent:
    def __init__(self):
        self.__private_var = "I am Private"
    def __private_method(self):
        print("Private Method Inside Parent")
    def access_private(self):
        print("Accessing Private Variable:", self.__private_var)
        self.__private_method()
class Main:
    def main_method(self):
        obj = Parent()
        obj.access_private()
        class Child(Parent):
            def child_method(self):
                print("Cannot access private members in subclass")
        child_obj = Child()
        child_obj.child_method()
if __name__ == "__main__":
    Main().main_method()


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


#Create a class with PUBLIC fields and methods.  
# Access the public methods and fields from any class in the same package or different package.
class Parent:
    def __init__(self):
        self.public_var = "I am Public"
    def public_method(self):
        print("Public Method Inside Parent")
class SamePackage:
    def access_public(self):
        obj = Parent()
        print("Accessing Public Variable:", obj.public_var)
        obj.public_method()
class DifferentPackage:
    def access_public(self):
        obj = Parent()
        print("Accessing Public Variable from Different Class:", obj.public_var)
        obj.public_method()
if __name__ == "__main__":
    obj1 = SamePackage()
    obj1.access_public()
    obj2 = DifferentPackage()
    obj2.access_public()