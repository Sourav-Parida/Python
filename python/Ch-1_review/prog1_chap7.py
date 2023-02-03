#Perform division of two numbers
num1 = 0
while num1!=100:
    try:
        num1=eval(input("Enter dividend = "))
        num2=eval(input("Enter divisor = "))
        num3 = num1//num2
        print("The quotient is =",num3)
    except NameError: print("Variable not present")
    except ZeroDivisionError: print("Division by zero not allowed")
    except: print("An error has occured")
    finally: print("Done!!!!")
    
        
        
