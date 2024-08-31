# changing the function of +

class ComplesNumber:
    def __init__(self,r,i) -> None:
        self.real = r
        self.imaginary = i
    
    def __add__(self,other):
        return str(self.real + other.real) + "+" + str(self.imaginary + other.imaginary) + "i"
        
 
C1 = ComplesNumber(2,4)
C2 = ComplesNumber(1,6)

print(C1 + C2)