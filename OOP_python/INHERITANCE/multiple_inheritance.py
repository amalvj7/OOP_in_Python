class Parent1:
    def __init__(self,object_mom_call):
        self.parent_1_name = "jaya"
        self.mom_calling = object_mom_call 
        
    def greet(self):
        print("Hello from Parent1")

class Parent2:
    def __init__(self,object_dad_call) :
        self.parent_2_name  = "vijayakumar"
        self.dad_calling = object_dad_call

    def greet(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    def __init__(self,object_mom_call,object_dad_call):
        Parent1.__init__(self,object_mom_call)
        Parent2.__init__(self,object_dad_call)
        self.child_name = "amal"

    def greet(self):
        Parent1.greet(self)
        Parent2.greet(self)
        print("Hello from Child")

    def cry(self):
        print("child is crying")

    def call_parent(self):
        print(f"i call my mom as {child_1.parent_1_name}")
        print(f"i call my dad as {child_1.parent_2_name}")
        print(f"my teachers call me as {self.child_name}")


child_1 = Child("makallee" , "lae")

child_1.greet()
child_1.cry()

print()

print(child_1.parent_1_name)
print(child_1.parent_2_name)
print(child_1.child_name)

print()

print(child_1.mom_calling)
print(child_1.dad_calling)

print()

child_1.call_parent()