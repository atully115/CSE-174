# Ashton Tully
# Dr. Goodman
# CSE 174
# Class assignment
# September 18 2024
"""Practicing while loops"""

import random

def rand_num():
    random_num = int(random.random() * 100) + 1
    stop = False
    count = 0
    print('Guess a number between 1 and 100: ', end = '')
    while (stop != True):
        guess = int(input())
        if (guess == random_num):
            stop = True
            break
        elif (guess < random_num):
            print('The number to guess is larger than what you guessed, ' +
                  'guess again: ', end = '')
        elif (guess > random_num):
            print('The number to guess is smaller than what you guessed, ' +
                  'guess again: ', end = '')
        count += 1
    print('You guessed correctly!\nIt took you %d guesses.' % (count))
    
def word_count():
    print('Enter a series of words, one at a time, to count them. Enter ' +
          '"done" to finish: ', end = '')
    count = 0
    word = ''
    while(word != 'done'):
        word = input().lower()
        if(word == 'done'):
            break
        count += 1
        print('Enter another word: ', end = '')
    print('Total words entered by user: %d' % (count))
    
def main():
    rand_num()
    word_count()
    
# Using the variable __name__
if __name__=="__main__":
    main()
