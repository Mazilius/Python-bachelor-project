names = []

while len(names) <= 2:
     question = input("Hello, would you like to add players to the team? \nY/N ")
     if question.isdigit():
        print("No numbers!")
        continue
   
     if question.lower() == "yes":
        player_names = input("Enter the name of the player to add to the team ")

        if player_names.isdigit():
            print("No numbers!")
            continue

        names.append(player_names) 
       
     elif question.lower() == "no":
        print(names)
        break
   

print("Player number 1 {}".format(names[0]))
print("Player number 2 {}".format(names[1]))
print("Player number 3 {}".format(names[2]))

goalkeeper = int(input("Who do you want as goalkeeper? "))

if goalkeeper == 1:
    print("The goalkeeper is {}".format(names[0]))
elif goalkeeper == 2:
    print("The goalkeeper is {}".format(names[1]))
elif goalkeeper == 3:
    print("The goalkeeper is {}".format(names[2]))
else:
    print("Invalid input!")
