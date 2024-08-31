class Human():
    def __init__(self,object_age,object_cllge) :
        self.age = object_age
        self.cllge = object_cllge

    def eat(self):
        print("i can eat")
    def sleep(self):
        print("i can sleep")
    def work(self):
        print("i can work")


class Man(Human):
    def __init__(self, object_age, object_cllge,object_rollno):
        super().__init__(object_age, object_cllge)
        self.roll_no = object_rollno

    def work(self):
        super().work() # include both the propertity of work fn , ie from parent class and child class
        print("i can code")

amal = Man(21,"CET" , 15)

amal.eat()
amal.work()
print(amal.roll_no)


# ie if we use the same fn in the child and the parent class , then have to add super() to get the both property