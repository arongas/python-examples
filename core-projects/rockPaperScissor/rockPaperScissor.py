import random
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

figures = [rock,paper,scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userChoice == 0 or userChoice == 1 or userChoice == 2:
    print(figures[userChoice])

if userChoice < 0 or userChoice > 2:
    print("Invalid selection")
else:
    computerChoice = random.randint(0, 2)
    print('Computer Chose:')
    print(figures[computerChoice])

    if computerChoice == userChoice:
        print("draw")
    elif computerChoice == 2 and userChoice == 0:
        print("You lose")
    elif computerChoice == 0 and userChoice == 2:
        print("You win")
    elif computerChoice > userChoice:
        print("You lose")
    else:
        print("You win")


