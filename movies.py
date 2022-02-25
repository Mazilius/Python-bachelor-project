import sys as s
import math as m

#-------------------------------------------------------------------------------------#
attempt = 3
"""""
This while loop confirms if the user is legal to watch movies and what movies they can see
"""""
while True:
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Value is not valid!")
    else: 
        if age <= 13:
            print(f"You are not old enough! You have {attempt} attempts left")
            attempt -= 1
            if attempt < 0:
                s.exit("Too many invalid tries!")
        elif age >= 13 and age <= 18:
            print("Welcome to the movies!")

            name = input("What is your name? ").capitalize()
            if name.isdigit():
                print("No numbers")
                continue
            else:
                print(f"Welcome to the python movies, {name}")
                break
        else:
            print("You can see the PG 18 movies alone!")
            name = input("What is your name? ").capitalize()
            if name.isdigit():
                print("No numbers")
                continue
            print(f"Welcome to the python movies, {name}")
            break


"""""
Calculation of ticket prices
"""""
TICKET_PRICE = 10
TICKET_AMOUNT = 5
SERVICE_CHARGE = 3


def calculator(tickets):
    return tickets * TICKET_PRICE + SERVICE_CHARGE

while TICKET_AMOUNT >= 1:
    print(f"There are {TICKET_AMOUNT} remaining and the price is ${TICKET_PRICE} per ticket and ${SERVICE_CHARGE} for the use of service")
    try:
        number_of_tickets = int(input("How many tickets you want? "))
        if number_of_tickets > TICKET_AMOUNT or number_of_tickets == 0:
            raise ValueError("Not enough tickets!")
    except ValueError as err:
        print(f"Invalid input! \n({err})")
    else:
        total_due = calculator(number_of_tickets)
        print(f"The total price is ${total_due}")
        TICKET_AMOUNT -= number_of_tickets
        break

def split_price():
    return m.ceil(total_due / number_of_tickets)

while number_of_tickets >= 2:
    print("We see that you have brought friends so the tickets will be divided")
    total_due = split_price()
    print(f"Each person has to pay ${total_due}")
    break
