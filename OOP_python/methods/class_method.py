class People():
    def __init__(self,object_cllge,object_age , object_backlogs = 0) :
        self.college = object_cllge
        self.age = object_age
        self.backlogs  = object_backlogs # this is asigned to every object


    def branch(self, year):
        print(f"i am doing b.tech in CS at {self.college}  right now in {year}th year ")

    def active_backlogs(self,subject):
        self.backlogs =+ 1
        print(f"backlog of abishek is {self.backlogs} and the subject he failed is {subject}")


amal = People("CET" , 21)
amal.branch(4)

abishek = People("SRM" , 21 )
abishek.active_backlogs("OOP")

#now u can understand when we calling the mthids and attributes we did want to write each time
#Also we didnot know what inside the function === abstraction