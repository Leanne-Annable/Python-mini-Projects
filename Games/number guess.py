#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
logo = """
 _   _                 _                                           
| \ | |               | |                                          
|  \| |_   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __|
| |\  | |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ \ 
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/
                                          __/ |                    
                                         |___/                     
"""
game_over = False
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
computer_choice = random.randint(1,100)
difficulty = input("Chose a difficulty, type 'easy' or 'hard': ").lower()

attempts = 0
if difficulty == "easy":
    attempts += 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty == "hard":
    attempts += 5
    print(f"You have {attempts} attempts remaining to guess the number.")
while not game_over:        
    # Allow the player to submit a guess for a number between 1 and 100.
    guess = int(input("Make a guess: "))
    if guess > 100 or guess < 1:
        print("You have guessed outside of the range, i need a number between 1-100")
        game_over = True
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
    elif guess != computer_choice:
        if guess > computer_choice:
            print("Too High")
            print("Guess again")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("Too low")
            print("Guess again")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number.")
    # If they got the answer correct, show the actual answer to the player.
    if guess == computer_choice:
        print(f"You guessed the correct number {computer_choice}! You win!")
        game_over = True
    # Track the number of turns remaining.
    
    # If they run out of turns, provide feedback to the player. 
    if attempts == 0:
        print("You ran out of attempts, game over.")
        game_over = True
    # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
    
