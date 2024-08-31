class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"
    
    def public_method(self):
        print("This is a public method")

obj = MyClass()
print(obj.public_attribute)  # Accessible from outside the class
obj.public_method()           # Accessible from outside the class
