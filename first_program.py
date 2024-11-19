# Name: Ashton Tully
# Cse 174, Section J
# Date: August 30, 2024
# Descripting: Practicing with writing, saving
#              and compiling code.

import random

# Prints a personalized welcome message to the user.
def welcome(name):
    print('Welcome, ' + name + '.')
    print('This is my first CSE 174 programming assignment.')
    print("Let's play"  + ' "Gues my number".')
    
# Explains the rules of the game.
def game_rules(name):
    print('Are you ready to plpay a game, ' + name + '?')
    print('I will think of a number between 1 and 50.')
    print('Try to guess it in 5 or fewer tries.')

# Draws a border made of asterisks
def draw_border(length):
    for i in range(length):
        print('*', end = '')
    print('')
        
    
    
def main():
    # Get user's first and last name
    print('What is your first and last name?')
    first = input()
    last = input()
    
    # Display border and greeting 
    draw_border(50)
    welcome(first)
    draw_border(50)
    
    # Explain the rules
    game_rules(first)
    
    # Start the game with a random number
    correct_number = random.randint(1, 50)
    guess_count = 0
    
    # Get first guess
    guess_count += 1
    print('Enter guess #' + str(guess_count) + ': ', end = '')
    guess = int(input())
    
    # Loop until th eguess is correct 
    while(guess != correct_number):
        # High or lower?
        if(guess < correct_number):
            print('GUess higher.')
        else:
            print('Guess lower.')
        
        guess_count += 1
        print('Enter guess #' + str(guess_count) + ': ', end = '')
        guess = int(input())
        
    print('Congratulations, ' + first + '.')
    print('You got it int ' + str(guess_count) + ' guesses')
    
    if(guess_count <= 5):
        print('You are an excellent guesser. :)')
    else: 
        print('Try harder next time. :(')
        
    #Display some art
    print('')
    print('And now, some stars to make you happy!')
    
    triangle_size = 7
    for length in range(triangle_size, 0, -1):
        draw_border(length)
        
    print('Goodbye!')
    
    
    
    
# using the special variable __name__

if __name__=="__main__":
    main()