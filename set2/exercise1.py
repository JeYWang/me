"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['additional word', 'word', 'what', 'does', 'this', 'line', 'do', '?']

#I think this prints "word"
for word in some_words:
    print(word)
    print('break')
    #this prints each item in the list, plus 'break' which I've added to test how it works.

#I think this does the same thing as the previous function 
for x in some_words:
    print(x)
    #this is doing exactly what the prev function does, just with a different name for the variable

#this prints the list of words
print(some_words)

#if length of this string is longer than 3, it prints what's written in the brackets
if len(some_words) > 3:
    print('some_words contains more than 3 words') #it printed what's in the brackets

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())
    #this identifies the current operating system, including name of OS, name of machine on the system, current release, version and hardware identifier

usefulFunction()
