# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0

    # Write your code in here

    guessed_number = int((low + high) / 2)

    while actual_number != guessed_number:
        if actual_number == guessed_number:
            guessed_number = guess
            return {"guess": guess, "tries": tries}
        elif actual_number - 2 < guessed_number < actual_number:
            tries = tries + 1
            guessed_number = guessed_number + 1
        elif actual_number < guessed_number:
            tries = tries + 1
            guessed_number = int(guessed_number / 2)
        elif actual_number > guessed_number:
            tries = tries + 1
            guessed_number = int((guessed_number + high) * 3)

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
