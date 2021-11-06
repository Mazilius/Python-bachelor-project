names = []


while len(names) <= 2:
     question = input("Hello, would you like to add players to the team? \nY/N ")
     if question.isdigit():
        print("No numbers!")
        continue
   
     if question.lower() == "yes":
        names = input("Enter the name of the player to add to the team ")

        if names.isdigit():
            print("No numbers!")
            continue

        names.append(names) 
       
     elif question.lower() == "no":
        print(names)
        break
   
print("There are {} players on this team!".format(len(names)))

player_number = 1
for player in names:
    print("Player {}: {}".format(player_number, player))
    player_number += 1


goalkeeper = int(input("Who do you want as goalkeeper? "))

if goalkeeper == 1:
    print("The goalkeeper is {}".format(names[0]))
elif goalkeeper == 2:
    print("The goalkeeper is {}".format(names[1]))
elif goalkeeper == 3:
    print("The goalkeeper is {}".format(names[2]))
else:
    print("Invalid input!")
