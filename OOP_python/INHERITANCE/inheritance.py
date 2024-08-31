class Human():
    def eat(self):
        print("i can eat")
    def sleep(self):
        print("i can sleep")


class Man(Human):
    def work(self):
        print("i can work")

amal = Man()

amal.eat()
amal.sleep()

