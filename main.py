from data import data
from art import  *
from random import choice


choice_one = choice(data)
choice_two = choice(data)
value_A = choice_one['follower_count']
value_B = choice_two['follower_count']

def compare(value_a, value_b):
  ...




print(f"Compare A: {choice_one['name']}, {choice_one['description']}, from {choice_one['country']}")
print(f"Compare A: {choice_two['name']}, {choice_two['description']}, from {choice_two['country']}")