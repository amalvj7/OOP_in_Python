# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Derived class 1 (Single Inheritance from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    
    def display_employee_info(self):
        return f"{self.display_person_info()}, Employee ID: {self.employee_id}"

# Derived class 2 (Single Inheritance from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display_student_info(self):
        return f"{self.display_person_info()}, Student ID: {self.student_id}"

# Hybrid Inheritance (Inheriting from both Employee and Student)
class WorkingStudent(Employee, Student):
    def __init__(self, name, age, employee_id, student_id):
        Employee.__init__(self, name, age, employee_id)
        Student.__init__(self, name, age, student_id)
    
    def display_info(self):
        return f"{self.display_employee_info()}, Student ID: {self.student_id}"

# Creating an object of the WorkingStudent class
ws = WorkingStudent("Amal", 21, "E123", "S456")

print(ws.display_info())
