# Base class
class Animal:
    def __init__(self, name):
        self.name = name
        self.no_of_eyes = 2

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class 1
class Dog(Animal):
    def speak(self):
        print( f"{self.name} barks")

    def eyes(self):
        print(f"{self.name} has {self.no_of_eyes} eyes")

# Derived class 2
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")


dog = Dog("Buddy")
cat = Cat("Whiskers")


dog.eyes()
