import random
from operator import index

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock,paper,scissors]

random_RPS = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors... \n"))
print("You Chose: ")
if random_RPS == 0:
    print(rock)
elif random_RPS == 1:
    print(paper)
elif random_RPS == 2:
    print(scissors)
else:
    print("Stop being cute and follow the rules! ")
# print("Computer Chose: ")
# game_results = print(random.choice(rock_paper_scissors))

computer_choice = random.randint(0,2)
# print(f"Computer Chose: {computer_choice}" )
print("Computer Chose...")
if computer_choice == 0:
    print(rock)
if computer_choice == 1:
    print(paper)
if computer_choice == 2:
    print(scissors)
# if random_RPS >= 3 or random_RPS < 0:
#     print("WRONG-O")
if random_RPS == 0 and computer_choice == 2:
    print("User Wins!")
elif random_RPS == 2 and computer_choice == 0:
    print("User Loses!")
elif random_RPS == 2 and computer_choice == 1:
    print("User Wins!")
elif computer_choice > random_RPS:
    print ("User Loses!")
elif random_RPS == computer_choice:
    print("You tie!")








