#working loop - write code, run code, fix code
#import random function and artwork from other files
import random
from art import logo
from art import vs
from game_data import data
import os
def clear():
    os.system( 'cls' )

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def compare(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    # if guess == "A":
      #     return True
      # else:
      #     return False
      # can also be written simpler as:
    return guess == "A"
  # This is stating if A is greater than B, and the guess was A, statement is true, else is false
  else:
    return guess == "B"
  # In this instance, if B has more followers and the guess was also B it will return True

def game():
    print(logo)
    score = 0
    game_over = False
    account_b = get_random_account()
    # We only need a value for account_b at this point as account_a will be dealt with in the repeatable step.    

    # Make game repeatable
    while not game_over:
        account_a = account_b
        account_b = get_random_account()
        # account_a now has the value of account_b and account_b gets a new value
        # need to make sure the two aren't the same
        if account_a == account_b:
          account_b = get_random_account()
          

        print(f"compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

    # Ask user for guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    # Check if user is correct
    ## Get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = compare(guess, a_follower_count, b_follower_count)
        
        # Clear screen after every guess
        clear()
        print(logo)
        # Give user feedback on their guess
        if is_correct:
            score += 1
            print(f"You're right! current score: {score}.\n")
        else:
            game_over = True
            print(f"Sorry, that was wrong. Final score: {score}.")

game()