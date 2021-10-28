print("Hello welcome to the simple calculator")


while True:
    operation = input("Press A for addition, S for substraction, M for multiplication, D for division ").upper()
    x = int(input("What is the first value? "))
    y = int(input("What is the second value? "))
    if operation == 'A':
        
        """
        Addition function
        """
        def addition(x, y): 
            return x + y

        print(addition(x, y))
        
    elif operation == 'S':
        """
        Substraction function
        """
        def substraction(x, y):
            return x - y
        print(substraction(x, y))
    elif operation == 'M':
        """
        Multiplication function
        """
        def multiplication(x, y):
            return x * y
        print(multiplication(x, y))
    elif operation == 'D':
        """
        Division function
        """
        def division(x,y):
            return x / y
        print(division(x, y))
    else:
        print("Invalid input!")
        
    q = input("Do you want another go? Type N if you want to quit ").upper()
    if q == "N":
        break
    else:
        print("Having another go!")
