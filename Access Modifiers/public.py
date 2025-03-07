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