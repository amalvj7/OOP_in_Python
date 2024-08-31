class Calculator:
    def add(self, *args):
        return sum(args)

# Create an instance of Calculator
calc = Calculator()

# Call the add method with different numbers of arguments
print(calc.add(2, 3, 4))  # Output: 9
print(calc.add(2, 3))     # Output: 5
print(calc.add(2))        # Output: 2
print(calc.add())         # Output: 0
