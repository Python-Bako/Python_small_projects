
# small script for guessing a random number

import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0

    while guess != random_num:
        guess = int(input(f"Enter a random number between 1 and {x}: "))
        if guess > random_num:
            print("Sorry, guess again. Too high!")
        elif guess < random_num:
            print("Sorry, guess again. Too low!")
        # there is no need to add an else statement since if the guess == random_num then we are exiting the while loop
    print(f"Congats you have guessed the number!!!!!!")
    print("make a change")

guess(10)


def calc_divide(x,y):
    return(x/y)