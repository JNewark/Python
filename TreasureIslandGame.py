print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
turn = input("You see two paths in front of you, do you take the left path or right path? ")
if turn == "left":
    print("You walk down the path...")
    water_trap = input("You come to a river that's deep but looks refreshing...do you swim across or wait for a boat?")
    if water_trap == "wait" and "wait for a boat":
        print("You glide across the water effortlessly....")
        door_choice = input("A man approaches and offers you three doors, red, green, and blue... ")
        if door_choice == "red":
            print("You found the treasure! You're rich!")
        elif door_choice == "green":
            print("The door explodes and you die. Game Over")
        elif door_choice == "blue":
            print("You're forced to watch anime until your eyes bleed...Game Over")
        else:
            print("The man judges you for not picking a door like he said, you die from embarrassment....Game Over")
    else:
        print("You are eaten by a Hungry Hungry Hippo.....Game Over")
else:
    print("A coconut falls on your head and you die....Game Over")

