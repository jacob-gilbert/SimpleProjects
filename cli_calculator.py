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
    
    def compute(self, line):
        # keep track of the numbers and operations in our line of input, this will allow us to
        # maintain pemdas ordering of operations
        num_list = []
        
        # remove whitespace from the line
        line = line.strip()
        
        # want to check if two operations are given in a row so we will remember if the previous character was an operation using a true or false
        # if given 24 we will first get the "2" char so when we get to "4" we want to be able to put it together with 20
        has_op = False
        was_mult_div = False
        prev_op = None
        
        has_prev_num = False
        prev_number = 0
        
        last_was_num = False
        
        for i in range(len(line)):
            char = line[i] # identify character
            ascii_val = ord(char) # determine ascii value of the character
            
            if 47 < ascii_val < 60:
                # determine which number the ascii value is
                number = ascii_val - 48
                
                # if there was no previous number to this one, the multiplication will result in 0
                # so the addition will just be the number we received and zero
                # otherwise we will adjust the previous digit by ten and add our new one
                prev_number = self.addition(self.multiplication(prev_number, 10), number)
                has_prev_num = True
                last_was_num = True
            
            # not a number
            else:
                # verify that a number was given previously (cannot have two operations in a row)
                if not last_was_num:
                    return "Error: Operation given before a number was given or two operations given in a row"
                
                # check if an operation was given previously then we have two numbers and an operation
                if has_op:
                    last_saved = num_list[-1]
                    
                    if was_mult_div:
                        if prev_op == "m":
                            num_list[-1] = last_saved * prev_number
                        else:
                            num_list[-1] = last_saved / prev_number
                    elif prev_op == "s":
                        num_list[-1] = last_saved - prev_number
                    else:
                        num_list[-1] = last_saved + prev_number
                        
                    has_op = False
                    was_mult_div = False
                    prev_op = None
                    
                
                # ignore spaces    
                if ascii_val == 32:
                    continue
                
                # must be an operation at this point or a value that doesn't correlate with any acceptable symbol
                
                # verify that a number was given previously before the operation
                if not has_prev_num:
                    return "Error: Operation given before a number"
                    
                # when an operation is found, the previous number must've been accounted for so store it in the list
                num_list.append(prev_number)
                prev_number = 0 # reset prev_number since it has been stored in a list
                    
                if ascii_val == 42:
                    was_mult_div = True
                    prev_op = "m"
                        
                elif ascii_val == 47:
                    was_mult_div = True
                    prev_op = "d" 
                    
                elif ascii_val == 43:
                    was_mult_div = False
                    prev_op = "a"
                    
                elif ascii_val == 45:
                    was_mult_div = False
                    prev_op = "s"
                    
                else:
                    return "Error: Unrecognized symbol given"
                
                # must have a recognized operation at this point
                has_op = True


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
    
    # run calculator's compute to determine answer in the inputted line
    print(calculator.compute(line))