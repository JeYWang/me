"""Correct the syntax in this file.

This file doesn't run yet.
Go through it and change it until it runs.
Remeber that all files must also pass the
linter with no errors or warnings!
"""
#linting: Linting highlights syntactical and stylistic problems in your Python source code, 
    # which often helps you identify and correct subtle programming errors 
    # or unconventional coding practices that can lead to errors.

import string

def getLetter(index):
    alphabet = string.ascii_lowercase + " "
    #In Python3, ascii_lowercase is a pre-initialized string used as string constant. 
    # In Python, string ascii_lowercase will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.
    return alphabet[index]
#index is where the item sits inside a list
# [] is the only way to make python recognise your number is an INDEX and not a STRING


def set2exercise2():
    indices = [12, 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = [getLetter(x) for x in indices]
    #map runs the function for each iterator/item, as defined by a previous function
    wordArray[0] = wordArray[0].upper()
    wordArray[1] = wordArray[1].upper()
    wordArray[3]= wordArray[3].upper()
    secret_word="".join(wordArray)
    # the "" defines what goes between strings as they're being joined
    print(secret_word)
    return secret_word
    #return command tells the computer that this is the end result, whereas print just prints it without associations


if __name__ == "__main__":
    hero = set2exercise2()
    print(hero)
    #one = is a forumla, and == is comparing left and right sides