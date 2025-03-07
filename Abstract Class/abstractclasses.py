from abc import ABC, abstractmethod

# 1. Create an abstract class with abstract and non-abstract methods
class Animal(ABC):  
    def sleep(self):  
        print("Animal is sleeping")

    @abstractmethod
    def make_sound(self): 
        pass

# 2. Create a subclass for an abstract class.
# Create an object in the child class for the abstract class and access the non-abstract methods
class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof! Woof!")

dog_obj = Dog()
dog_obj.sleep()  

# 3. Create an instance for the child class in child class and call abstract methods
class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow! Meow!")

    def call_make_sound(self):
        self.make_sound()

cat_obj = Cat()
cat_obj.call_make_sound() 

# 4. Create an instance for the child class in child class and call non-abstract methods
class Cow(Animal):
    def make_sound(self):
        print("Cow says: Moo! Moo!")

    def call_sleep(self):
        self.sleep()

cow_obj = Cow()
cow_obj.call_sleep() 