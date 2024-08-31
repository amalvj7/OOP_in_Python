from abstract_class import Vehicle

class Car(Vehicle):
    def start(self):
        print(f"The car with {self.no_of_tyres} tyres is starting.")

# Another subclass
class Bike(Vehicle):
    def start(self):
        print(f"The bike with {self.no_of_tyres} tyres is starting.")