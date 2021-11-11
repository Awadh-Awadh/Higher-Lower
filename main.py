from data import data
from art import  *
from random import choice


def compare(guess,value_a, value_b):
    """
      Check if user is correct
      Takes the users guess and follower count and returns if they got it right
      Returns a boolean
    """

    if value_a > value_b:
      #return True if guess is 'a'
       return guess == 'a'
    else:
        return guess == "b"
# Display art
print(logo)
score = 0
game_should_continue = True
choice_two = choice(data)


# make the game repeatable

while game_should_continue:
    # generate a random account from the game data
    choice_one = choice_two
    choice_two = choice(data)

    """make sure accounts are not simmilar"""
    while choice_two == choice_one:
      choice_two = choice(data)

    # Format choices into printable data
    print(f"Compare A: {choice_one['name']}, {choice_one['description']}, from {choice_one['country']}")
    print(vs)
    print(f"Against B: {choice_two['name']}, {choice_two['description']}, from {choice_two['country']}")


    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check user if is correct
    value_A = choice_one['follower_count']
    value_B = choice_two['follower_count']

    is_correct = compare(guess, value_A, value_B)

    # Give user feedback
    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}")
    else:
        game_should_continue = False
        print(f"You got it wrong.Final score: {score}")

# make the account at position B be at the first position in the next iteration

"""
make choice B a global variable
set choice a = the choice b global variable
generate a new choice b in the loop


"""