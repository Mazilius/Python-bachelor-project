print("Hello welcome to the simple calculator")

operation = input("Press A for addition, S for substraction, M for multiplication, D for division ").upper()
if operation == 'A':
    x = int(input("What is the first value? "))
    y = int(input("What is the second value? "))
    """
    Addition function
    """
    def addition(x, y): 
        return x + y

    print(addition(x, y))
elif operation == 'S':
    x = int(input("What is the first value? "))
    y = int(input("What is the second value? "))
    """
    Substraction function
    """
    def substraction(x, y):
        return x - y
    print(substraction(x, y))
elif operation == 'M':
    x = int(input("What is the first value? "))
    y = int(input("What is the second value? "))
    """
    Multiplication function
    """
    def multiplication(x, y):
        return x * y
    print(multiplication(x, y))
elif operation == 'D':
    x = float(input("What is the first value? "))
    y = float(input("What is the second value? "))
    """
    Division function
    """
    def division(x,y):
        return x / y
    print(division(x, y))
else:
    print("Invalid input!")

