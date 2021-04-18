# Lab 1 - Guess the Number Game, Version 1
# Version 1 is also the full version.
# It read's the users guess
# It displays the value selected by the program, and then the user's guess


import random

def main():
    # display instructions
    print('I am thinking of a number between 1 and 10.')
    program_selection = random.randint(1,10)    # randomly pick an integer between 1 and 10
    
    user_guess = input('What is the number?')  # get player guess
    print('The number was ' + str(program_selection) + '.')
    print('You guessed ' + str(user_guess) + '.')
 
main()