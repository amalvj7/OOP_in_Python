class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Human:
    def speak(self):
        return "Hello!"

# Function that accepts any object with a 'speak' method
def make_it_speak(animal):
    print(animal.speak())

# Using the function with different objects
dog = Dog()
cat = Cat()
human = Human()

make_it_speak(dog)    # Output: Woof!
make_it_speak(cat)    # Output: Meow!
make_it_speak(human)  # Output: Hello!
