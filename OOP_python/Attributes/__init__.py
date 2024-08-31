#without __init__ method

class Animal():
    pass

dog = Animal()
dog.name = "doni"
dog.age = 21


cat = Animal()
cat.name = "puuna"
cat.age = 10

print(cat.age)
print(dog.name)


print()
#with __init__ method
#ie if we us the __init__  the attributes and  methods can be given in the class itself

class People():
    def __init__(self,object_cllge,object_age, object_gender ="male") :
        self.college = object_cllge
        self.age = object_age
        self.gender  = object_gender # this is asigned to every object

amal = People("CET" , 21)
abishek = People("SRM",20)

print(amal.college)
print(abishek.age)
print(amal.gender)

anjana = People("ABC College", 25, "female")  # Specified gender is "female"

print(anjana.gender)  