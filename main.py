from data import data
from art import  *
from random import choice


def compare(value_a, value_b):
   """Check if user is correct"""
#Display art
print(logo)

#generate a random account from the game data
choice_one = choice(data)
choice_two = choice(data)
if choice_two == choice_one:
  choice_two = choice(data)

#Format choices into printable data
print(f"Compare A: {choice_one['name']}, {choice_one['description']}, from {choice_one['country']}")
print(vs)
print(f"Against B: {choice_two['name']}, {choice_two['description']}, from {choice_two['country']}")


#Ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#check user if is correct
value_A = choice_one['follower_count']
value_B = choice_two['follower_count']
 

   