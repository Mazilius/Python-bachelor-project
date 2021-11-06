player_names = []


while len(player_names) <= 2:
     question = input("Hello, would you like to add players to the team? \nY/N ")
     if question.isdigit():
        print("No numbers!")
        continue
   
     if question.lower() == "yes":
        player_names = input("Enter the name of the player to add to the team ")

        if player_names.isdigit():
            print("No numbers!")
            continue

        player_names.append(player_names) 
       
     elif question.lower() == "no":
        print(player_names)
        break
   
print("There are {} players on this team!".format(len(player_names)))

player_number = 1
for player in player_names:
    print("Player {}: {}".format(player_number, player))
    player_number += 1


goalkeeper = int(input("Who do you want as goalkeeper? "))

if goalkeeper == 1:
    print("The goalkeeper is {}".format(player_names[0]))
elif goalkeeper == 2:
    print("The goalkeeper is {}".format(player_names[1]))
elif goalkeeper == 3:
    print("The goalkeeper is {}".format(player_names[2]))
else:
    print("Invalid input!")
