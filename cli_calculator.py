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


# if user wants to use the calculator create a calculator instance to use
use_calc = input("Do you want to use the calculator? (y/n)\n")
if use_calc:
    calculator = CLI_Calculator()
   
# using a while loop so we can continuously use the calculator even after it has been used 
while use_calc:
    # take in user input and decide if the user wants to continue using the calculator
    print("Calculator is ready to be used")
    line = input("Type a line of math into the calculator to continue or 'n' to close\n")
    if line.lower() == "n":
        break
    
    