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
    else:  # If everything is valid with the value then the while loop will run
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

#Create a function here for calculating TICKET_PRICE * NUMBER OF TICKETS
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

#TODO: ask the user how many they are IF they have bought more than 1 ticket.

def split_price():
    return m.ceil(total_due / number_of_tickets)

while number_of_tickets >= 2:
    print("We see that you have brought friends so the tickets will be divided")
    equal_due = split_price()
    print(equal_due)
    break



#TODO: List which movies they can watch and pick one of them.
print("These are the movies you can watch!")