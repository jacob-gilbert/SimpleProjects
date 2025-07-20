class CLI_Calculator:
    def __init__(self):
        self.return_value = 0
    
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
                # ignore spaces    
                if ascii_val == 32:
                    continue
                
                # verify that a number was given previously (cannot have two operations in a row)
                if not last_was_num:
                    return "Error: Operation given before a number was given or two operations given in a row"
                
                # verify that a number was given previously before the operation
                if not has_prev_num:
                    return "Error: Operation given before a number"
                
                # check if an operation was given previously then we have two numbers and an operation
                if has_op:
                    last_saved = num_list[-1]
                    
                    # can do the mult/div operation immediately because they are first in order of ops
                    if was_mult_div:
                        if prev_op == "m":
                            num_list[-1] = last_saved * prev_number
                        else:
                            num_list[-1] = last_saved / prev_number
                            
                    # if its subtraction we don't do the subtraction yet because a mult or div could come next
                    elif prev_op == "s":
                        num_list.append(-prev_number)
                        
                    else:
                        num_list.append(prev_number)
                        
                    prev_number = 0 # reset prev_number since it has been stored in a list
                        
                    has_op = False
                    was_mult_div = False
                    prev_op = None
                else:
                    # this case is triggered after the first number is inputted, store it and reset prev_number var
                    num_list.append(prev_number)
                    prev_number = 0
                
                # must be an operation at this point or a value that doesn't correlate with any acceptable symbol
                    
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
                last_was_num = False
                
        # for loop has ended and the last operation has not been completed so do that now
        last_saved = num_list[-1]
                    
        if was_mult_div:
            if prev_op == "m":
                num_list[-1] = last_saved * prev_number
            else:
                num_list[-1] = last_saved / prev_number
        # since this is the last operation and all mult/div's have been done already it is safe to do these operations
        elif prev_op == "s":
            num_list[-1] = last_saved - prev_number
        else:
            num_list[-1] = last_saved + prev_number
            
        # all that is left are all the saved numbers that must be added together
        total = 0
        for i in range(len(num_list)):
            total += num_list[i]
        return total



# if user wants to use the calculator create a calculator instance to use
use_calc = input("Do you want to use the calculator? (y/n)\n")
if use_calc == "y":
    calculator = CLI_Calculator()
else:
    exit()
   
# using a while loop so we can continuously use the calculator even after it has been used 
while use_calc:
    # take in user input and decide if the user wants to continue using the calculator
    print("Calculator is ready to be used")
    line = input("Type a line of math into the calculator to continue or 'n' to close\n")
    if line.lower() == "n":
        break
    
    # run calculator's compute to determine answer in the inputted line
    print(calculator.compute(line))