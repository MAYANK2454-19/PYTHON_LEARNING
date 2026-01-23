#This is a game where the next step depends on your previous choice chhose the correct path and get to the treasure or else game over.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You are at a cross-road. Where do you want to go ? Type "left" or "right" \n')
lake = input('You come to a lake. There is an island in the middle of the lake . Type "wait" to wait for a boat or "swim" to swim across the lake\n')
door = input("You arrived at the island unharmed . Ther is a house with 3 doors . one red one yellow and one blue . which colour do you choose ?\n")

if direction =="left" or direction == "LEFT" :
    print(lake)
    if lake == "swim" or lake == "SWIM" :
        print("You were eaten by a crocodile !!!\n")
    elif lake == "wait" or lake == "WAIT" :
        print(door)
        if door == "red" or door == "RED" :
            print("You entered a room full or fire and died . game over .\n")    
        elif door == "yellow" or door == "YELLOW" :
            print("You entered a room full Beasts and they killed you . game over .\n")    
        elif door == "blue" or door == "blue" :
            print("HURRAY!!! , You have entered the correct room with treasue and You Won the game .\n")    

elif direction == "right" or direction == "RIGHT" :
    print("You fell into a deep hole. game over.\n")
else :
    print("Enter a valid direction .\n")
