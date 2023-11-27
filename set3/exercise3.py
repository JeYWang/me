"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def super_asker(low, high, message):
    """Robust asking function.
    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    while True:
        k = input(message)
        try:
            number = int(k)
            if low <= number <= high:
                return number
            else:
                print(f"Please pick a battle worth fighting - {k} seems out of reach, but we shall allow another go. ")
        except ValueError:
            print(f"Oh dear, you do know {k} isn't a number, right?")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)
      failure #1: entering something thats not a number
      failure #2: lower bound bigger than upper bound
      failure #3: lower bound same as upper bound

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print(
        "Welcome to the Arena, the good citizens of the Empire!/n"
        "Today we are here to defeat a few soldiers - a mystery sized army between _ and _ ? "
    )
    # /n - escape character for new line. "" - break up character

    lower_bound = super_asker(0, 50000, "How many to make this fight worthwile? ")
    upper_bound = super_asker(
        lower_bound+2, 50000, "How many would be too hard to beat? "
    )

    print(f"OK then, a troop sized between {lower_bound} and {upper_bound}? ")

    actual_number = random.randint(lower_bound, upper_bound)

    while True:
        guessed_number = super_asker(
            lower_bound,
            upper_bound,
            f"Guess a troop size between{lower_bound} and {upper_bound}",
        )
        print(f"You guessed {guessed_number},")
        if guessed_number == actual_number:
            print(f"You got it!! It was {actual_number}")
            return "You got it!"
        elif guessed_number < actual_number:
            guessed_number = input("There are enemies aplenty, larger troops at bay:  ")
        else:
            guessed_number = input(
                "Oh dear citizen, surely our Empire has more mercy! There are fewer than you think:  "
            )

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
