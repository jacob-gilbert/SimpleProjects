class CLI_Calculator:
    def __init__(self):
        self.return_value = 0
        
    def addition(self, num1, num2):
        return num1 + num2
    
    def subtraction(self, num1, num2):
        return num1 - num2
    
    def multiplication(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        return num1 / num2


use_calc = input("Do you want to use the calculator? (y/n)\n")
if use_calc:
    calculator = CLI_Calculator()
    
while use_calc:
    print("Calculator is ready to be used")
    line = input("Type a line of math into the calculator to continue or 'n' to close\n")
    if line.lower() == "n":
        break