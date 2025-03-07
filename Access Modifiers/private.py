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