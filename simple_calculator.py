print("Hello welcome to the simple calculator")

"""
Addition function
"""
def addition(x, y): 
    return x + y

"""
Substraction function
"""
def substraction(x, y):
    return x - y

"""
Multiplication function
"""
def multiplication(x, y):
    return x * y

"""
Division function
"""
def division(x,y):
    return x / y

while True:
    operation = input("Press A for addition, S for substraction, M for multiplication, D for division ").upper()

    if operation == 'A':
        x = int(input("What is the first value? "))
        y = int(input("What is the second value? "))
        total = int(addition(x, y))

        print(total)
    elif operation == 'S':
        x = int(input("What is the first value? "))
        y = int(input("What is the second value? "))
        total = int(substraction(x, y))
        
        print(total)
    elif operation == 'M':
        x = int(input("What is the first value? "))
        y = int(input("What is the second value? "))
        total = int(multiplication(x,y))

        print(total)
    elif operation == 'D':
        x = int(input("What is the first value? "))
        y = int(input("What is the second value? "))
        total = int(division(x,y))

        print(total)
    else:
        print("Invalid input!")
        
    q = input("Do you want another go? Type N if you want to quit ").upper()
    if q == "N":
        break
    else:
        print("Having another go!")


