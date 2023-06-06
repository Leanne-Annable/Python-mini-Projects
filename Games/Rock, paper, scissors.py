rock = '''
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ______
---'   ____)___
          ______)
          _______)
         _______)
---._________)
'''

scissors = '''
    ______
---'   ____)____
           ______)
       __________)
      (_____)
---.__(___)
'''

#Write your code below this line 👇
import random

images = [rock, paper, scissors]

user =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user >=3 or user < 0:
  print("You typed an invalid number, you lose!")
else:
  print(images[user])
  
  comp = random.randint(0,2)
  
  print("Computer chose:")
  print(images[comp])
  
  
  if user == 0 and comp == 2:
    print("You win!")
  elif comp == 0 and user == 2:
    print("You lose!") 
  elif comp > user:
    print("You lose!")
  elif user > comp:
    print("You win!")
  elif comp == user:
    print("It's a draw!")
