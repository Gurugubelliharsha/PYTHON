#Create a class with main method. 
# Create an object for each class A, B and C in main method and call every method of each class using its own object/instance. 
#Call an overridden method with super class reference to B and C class’s objects 
class A():
    def display(self):
        print("Display Inside class A")
    def show(self):
        print("Show Inside class A")
class B(A):
    def print(self):
        print("Print Inside class B")
    def show(self):
        print("Show Inside class B")
class C(B):
    def show(self):
        print("Show Inside class C")
s = A()
s.display()
k = B()
k.print()
g = C()
g.show()