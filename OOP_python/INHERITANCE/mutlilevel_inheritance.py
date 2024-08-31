class Grandparent:
    def __init__(self,husband_name):
        self.grandparent_husband_name = husband_name
        self.grandparent_name = "Thankam"
        
    def show_grandparent(self):
        print(f"Grandparent: {self.grandparent_name}")

class Parent(Grandparent):
    def __init__(self,husband_name):
        Grandparent.__init__(self,husband_name)
        self.parent_name = "jaya"
        
    def show_parent(self):
        print(f"Parent: {self.parent_name}")

class Child(Parent):
    def __init__(self,husband_name):
        Parent.__init__(self,husband_name)
        self.child_name = "amal"
        
    def show_child(self):
        print(f"Child: {self.child_name}")

# Creating an instance of Child
child_instance = Child("thomas")

# Accessing methods from all levels of inheritance


child_instance.show_child()
child_instance.show_parent()
child_instance.show_grandparent()

print(child_instance.grandparent_husband_name)

