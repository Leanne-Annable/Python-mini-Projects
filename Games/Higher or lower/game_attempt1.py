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
    return guess == "A"
  else:
    return guess == "B"

def game():
    print(logo)
    score = 0
    game_over = False
    account_a = get_random_account()
    account_b = get_random_account()

    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        print(f"compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = compare(guess, a_follower_count, b_follower_count)
        
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! current score: {score}.")
        else:
            game_over = True
            print(f"Sorry, that was wrong. Final score: {score}.")

game()