class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"
    
    def __private_method(self):
        print("This is a private method")

obj = MyClass()
# print(obj.__private_attribute)  # This will raise an AttributeError
# obj.__private_method()          # This will raise an AttributeError
