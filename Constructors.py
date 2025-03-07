# 1. Class with default, one-argument, and two-argument constructors
class Vehicle:
    def __init__(self, name="Unknown", speed=0):
        print("Vehicle:", name, "Speed:", speed)

v1 = Vehicle()
v2 = Vehicle("Car")
v3 = Vehicle("Bike", 80)

# 2. Call constructors of super class from child class
class Car(Vehicle):
    def __init__(self, name, speed, model):
        super().__init__(name, speed)
        print("Car Model:", model)

c1 = Car("Sedan", 120, "Toyota")

# 3. Apply private, public, protected, and default access modifiers to the constructor
class AccessModifiers:
    def __init__(self):
        print("Public Constructor")

    def __init_protected(self):
        print("Protected Constructor")

    def __init_private(self):
        print("Private Constructor")

am = AccessModifiers()

# 4. Program illustrating the concept of attributes of a constructor
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.name, "makes", self.sound)

dog = Animal("Dog", "Bark")
cat = Animal("Cat", "Meow")

dog.make_sound()
cat.make_sound()