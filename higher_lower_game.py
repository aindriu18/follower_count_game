import os
import random
from os import system
from game_art import logo, vs
from game_data import data

user_score = 0
#flag used to determine when game ends
user_correct = True
# generated outside of while loop so that celeb_b will also be in position 1 after the initial guess.
celeb_b = random.choice(data)
while user_correct:
    print(logo)

    # provide user with options at random
    celeb_a = random.choice(data)
    #making sure that celeb_b will position itself at position 1 when the user gets answer correct
    celeb_a = celeb_b
    celeb_b = random.choice(data)

    print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']} from {celeb_a['country']}.")

    print(vs)

    print((f"Against B: {celeb_b['name']}, a {celeb_b['description']} from {celeb_b['country']}."))


    # request input from user as to which is higher or lower.
    user_selection = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Cheeks if user selection is correct. Updates score if correct guess matches correct answer.
    if user_selection == 'A' and celeb_a['follower_count'] > celeb_b['follower_count']:
        user_score += 1
        print(f"You are correct. Your current score is {user_score}")
    elif user_selection == 'B' and celeb_b['follower_count'] > celeb_a['follower_count']:
        user_score += 1
        print(f"You are correct. Your current score is {user_score}")
    else:
        print(f"That is incorrect. Your final score is {user_score}")
        # Flag that will exit the game
        user_correct = False