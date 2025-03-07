# 1. Two methods with the same name but different number of parameters of the same type
class Example1:
    def add(self, a, b=0):
        print("Sum:", a + b)

e1 = Example1()
e1.add(5)
e1.add(5, 10)

# 2. Two methods with the same name but different number of parameters of different data types
class Example2:
    def show(self, a=None, b=None):
        print("Values:", a, b)

e2 = Example2()
e2.show(5)
e2.show("Hello", 10)

# 3. Two methods with the same name and same number of parameters of the same type
class Example3:
    def display(self, a, b):
        print("Numbers:", a, b)

e3 = Example3()
e3.display(5, 10)