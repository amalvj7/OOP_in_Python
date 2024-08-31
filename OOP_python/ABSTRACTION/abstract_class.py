from abc import ABC, abstractmethod  # Import ABC and abstractmethod

class Vehicle(ABC):  # Correcting the typo in class name
    def __init__(self, no_of_tyres) -> None:  # Renaming the parameter for clarity
        self.no_of_tyres = no_of_tyres

    @abstractmethod
    def start(self):
        pass




