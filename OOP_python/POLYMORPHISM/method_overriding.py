class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Using polymorphism
def make_animal_speak(animal):
    animal.speak()

# Creating instances of the subclasses
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Dog barks
make_animal_speak(cat)  # Output: Cat meows
