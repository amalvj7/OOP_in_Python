class University:
    def __init__(self,university_name) -> None:
        self.University_name = university_name

    def show_details(self):
        print(f"The university name is {self.University_name}")


class Course(University):
    def __init__(self,university_name,course_name,):
        super().__init__(university_name)
        self.Course_name = course_name

    def show_details(self):
        print(f"The course name is {self.Course_name}")
        print(f"the university belong this course is {self.University_name}")


class Branch(University):
    def __init__(self,university_name,branch_name) :
         super().__init__(university_name)
         self.Branch_name = branch_name



    def show_details(self):
        print(f"the branch_name is {self.Branch_name}")
        print(f"the university belong this course is {self.University_name}")

class Student_1(Branch,Course):
    def __init__(self, university_name, branch_name):
        super().__init__(university_name, branch_name)
    

class Faculty(Branch):
    pass

