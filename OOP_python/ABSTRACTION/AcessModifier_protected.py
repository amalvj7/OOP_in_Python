class MyClass:
    def __init__(self):
        self._protected_attribute = "I am protected"
    
    def _protected_method(self):
        print("This is a protected method")

obj = MyClass()
print(obj._protected_attribute)  # Can be accessed but is not recommended
obj._protected_method()           # Can be accessed but is not recommended
