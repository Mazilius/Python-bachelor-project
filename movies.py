import sys as s
import math as m
from tabulate import tabulate

#-------------------------------------------------------------------------------------#

print(""" 
Welcome to python movies!
There are different age criterias you have to meet in order to use our services
    - You must at least be the age of 13 in order to see PG 12
    - People between the age of 14 and 18 can are allowed to watch R15 movies
    - People aged 18 and above will be allowed to watch every available movie
Ticket prices are all the same for whatever age group you are in with a service charge include
""")

attempt = 3

def welcome():
    while True:
        username = input("What is your name? ").capitalize()
        if username.isdigit():
            print("No numbers")
        elif len(username) >= 14:
            print("Name is too long!")
        elif len(username) <= 3:
            print("Name is too short!")
        else:
            print(f"Welcome to Python movies, {username}. You will be proceeded to the available movie and later proceeded to the ticket venue \n")
            break
            
print()
    

"""""
This while loop confirms if the user is legal to watch movies and what movies they can see
"""""
while True:
    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Value is not valid!")
    else:  # If everything is valid with the value then the while loop will run
        if age <= 6:
            print(f"You are not old enough! You have {attempt} attempts left")
            attempt -= 1
            if attempt < 0:
                s.exit("Too many invalid tries!")
        elif age >= 6 and age <= 18:
            print("Welcome to the movies!")
            print("You are able to watch the following titles!")
            welcome()
            break
        else:
            print("Welcome to the movies!")
            print("You can watch every available movie!")
            welcome()
            break
         

"""""
Movie selection
"""""
#TODO: Add a list here with different movies, age restriction and how many tickets left
movie_list = [
    ["Black Widow", 13, 12],
    ["Django unchained", 18, 14], 
    ["Spider-Man: No Way Home", 13, 3],
    ["Avengers: Endgame", 13, 1],
    ["Winther on Fire: Ukraine's Fight for Freedom", 15, 17],
    ["Doctor Strange in the multiverse of madness", 11, 4],
    ["Fantastic Beasts 3", 11, 20],
    ["Sonic the Hedgehog 2", 7, 5],
    ["The Northman", 15, 24],
    ["Speak No Evil", 18, 7],
    ["C'mon C'mon", 18, 10],
    ["The Batman", 11, 4],
    ["Paris, 13th Distric", 15, 40],
    ["Morbius", 15, 4]
]

#TODO: Print the name values out of the nested list
movie_age_list = []

for movie in movie_list:
    if age >= movie[1]:
        movie_age_list.append(movie)
        
        


print(tabulate(movie_age_list, headers = ["Movie", "PG", "No. Tickets"], tablefmt="fancy_grid"))


#TODO: Pick a specific movie from the new list and show the ticket amounts
print("""
!Please notice that there are limited amount of tickets for every movie!
""")

#movie_selection = []
#while True:




#print("This is your desired movie!")
#print(tabulate(movie_selection, headers = ["Movie", "PG", "No. Tickets"], tablefmt="fancy_grid"))
#while True:
    #selection = input("Please type in your desired movie: ")
    #if selection not in movie_age_list:
    #    print("Movie is non existent")
    #else:
    #    movie_selection.append(selection) 
    #    break




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
    print(f"There are {TICKET_AMOUNT} tickets remaining and the price is ${TICKET_PRICE} per ticket and ${SERVICE_CHARGE} for the use of service")
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
    total_due = split_price()
    print(f"Each person has to pay ${total_due}")
    break
