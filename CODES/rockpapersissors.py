import random
# Rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
player = int(input("Enter your choice . 0 for rock , 1 for paper and 2 for scissors\n"))
self=random.randint(0,2)
if (player==0 and self ==0):
    print("You : ")
    print(rock)
    print("Computer : ")
    print(rock)
    print("Its a tie!")
elif (player==0 and self ==1):
    print("You : ")
    print(rock)
    print("Computer : ")
    print(paper)
    print("You lose!")
elif (player==0 and self ==2):
    print("You : ")
    print(rock)
    print("Computer : ")
    print(scissors)
    print("You won!")
elif (player==1 and self ==0):
    print("You : ")
    print(paper)
    print("Computer : ")
    print(rock)
    print("You won!")
elif (player==1 and self ==1):
    print("You : ")
    print(paper)
    print("Computer : ")
    print(paper)
    print("Its a tie!")
elif (player==1 and self ==2):
    print("You : ")
    print(paper)
    print("Computer : ")
    print(scissors)
    print("You lose!")
elif (player==2 and self ==0):
    print("You : ")
    print(scissors)
    print("Computer : ")
    print(rock)
    print("You lose!")
elif (player==2 and self ==1):
    print("You : ")
    print(scissors)
    print("Computer : ")
    print(paper)
    print("You won!")
elif (player==2 and self ==2):
    print("You : ")
    print(scissors)
    print("Computer : ")
    print(scissors)
    print("Its a tie!")
else :
    print("Invalid input!")