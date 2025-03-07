# 1.1 Create two classes with a constructor and a method for each class

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def details(self):
        print(f"{self.name} moves at {self.speed} km/h")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

# 1.2 Create an __init__.py for adding all packages
# (In actual projects, this file initializes packages)

# 1.3 Import the respective packages
# (we are keeping everything in one file, we don't need imports)

# 1.4 Call each class by creating an object to it

car = Vehicle("Car", 120)
bike = Vehicle("Bike", 80)

dog = Animal("Dog", "Woof! Woof!")
cat = Animal("Cat", "Meow! Meow!")

car.details()
bike.details()
dog.make_sound()
cat.make_sound()

# 1.5 Create a program by combining all the above
