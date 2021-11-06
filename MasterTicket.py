SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(tickets):
  return tickets * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining >= 1: 
    print("There are {} tickets remaining!".format(tickets_remaining))

    username = input("Welcome to the masterticket. \nWhat is your name? ")
    try:
      tickets = int(input("Hello {}, how many tickets would you like to buy? ".format(username)))
      if tickets > tickets_remaining:
        raise ValueError("Not enough tickets!")
    except ValueError as err: 
      print("Invalid value! {} Please try again".format(err))
    else:
      total_due = calculate_price(tickets)
      print("The total due is {} ".format(total_due))
      should_proceed = input("Do you want to proceed? Y/N ")
  
      if should_proceed.lower() == "y":
          print("SOLD!")
          tickets_remaining -= tickets
      else:
          print("Have a nice day, {}".format(username))

print("We are out of tickets. Sorry")