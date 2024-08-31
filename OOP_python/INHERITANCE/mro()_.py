class Parent1:
    def greet(self):
        print("Hello from Parent1")

class Parent2:
    def greet(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    def greet(self):
        print("Hello from Child")

# Creating an instance of Child
child = Child()

# Calling the greet method
#child.greet()

# Checking the Method Resolution Order
print(Child.mro())
