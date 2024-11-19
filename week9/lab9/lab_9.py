# Author: Ashton Tully
# Professor: Dr. Goodman
# CSE 174 J
# Date: 10/25/2024
# Lab 9
# Copyright: 2024 Ashton Tully
"""Purpose of this is to practice recursion"""

def power(x: int, n: int) -> int:
    """
    Recursively calculates the power of a given base number to a given exponent.
    
    Args:
        x (int): The base number.
        n (int): The exponent.
    
    Returns:
        int: The result of raising the base number to the given exponent.
    """
    if(n == 0):
        return 1
    return x * power(x, n - 1)

def sum_digits(n: int) -> int:
    """
    Recursively calculates the sum of the digits of a given integer.
    
    Args:
        n (int): The integer to sum the digits of.
    
    Returns:
        int: The sum of the digits of the given integer.
    """
    if(n == 0):
        return 0
    return (n % 10) + sum_digits(n // 10)

def num_vowels(word: str) -> int:
    """
    Recursively counts the number of vowels in a given string.
    
    Args:
        word (str): The string to count the vowels in.
    
    Returns:
        int: The number of vowels in the given string.
    """
    if(len(word) == 0):
        return 0
    if(word[0].lower() in 'aeiouy'):
        return 1 + num_vowels(word[1:])
    return num_vowels(word[1:])

def print_backwards(word: str) -> None:
    """
    Recursively prints the characters of the given string in reverse order.
    
    Args:
        word (str): The string to print in reverse order.
    
    Returns:
        None
    """
    if(len(word) == 0):
        return
    print(word[-1], end = '')
    print_backwards(word[:-1])

def max_digit(n: int) -> int:
    """
    Recursively finds the maximum digit in a given integer.
    
    Args:
        n (int): The integer to find the maximum digit of.
    
    Returns:
        int: The maximum digit in the given integer.
    """
    if(n < 10):
        return n
    return max(n % 10, max_digit(n // 10))


def menu() -> None:
    """
    Displays a menu of options for the user to choose from, including various recursive
    functions to perform on input data.
    """
    print('Enter a choice for one of the following problems: ')
    print('1. Power')
    print('2. Sum digits')
    print('3. Count vowels')
    print('4. Print backwards')
    print('5. Max digit of an integer')
    print('6. Exit the program')

def main():
    """
    Implements a menu-driven program that allows the user to choose from
    various recursive functions to perform on input data.
    
    The main function prompts the user to select an option from the menu,
    then calls the corresponding recursive function with user-provided
    input. The recursive functions include:
    
    - power(base, pow): Calculates the result of raising a base to a power.
    - sum_digits(n): Calculates the sum of the digits in an integer.
    - num_vowels(word): Counts the number of vowels in a string.
    - print_backwards(word): Prints the characters of a string in reverse order
    - max_digit(n): Finds the maximum digit in an integer.
    
    The program continues to run until the user selects the 'Exit the program' option.
    """
    choice = -1
    while(choice != 6):
        menu()
        choice = int(input())

        match(choice):
            case 1:
                print('Enter the base: ', end = '')
                base = int(input())
                print('Enter the power: ', end = '')
                pow = int(input())
                print('The result of taking the power of %d of base %d is %d.' \
                      % (pow, base, power(base, pow)))
            case 2:
                print('Enter the integer to sum the digits of: ', end = '')
                num = int(input())
                print('The result of summing the digits of the integer %d is %d.' \
                      % (num, sum_digits(num)))
            case 3:
                print('Enter the String of characters you want ' \
                      + 'to count the vowels of: ', end = '')
                word = input()
                print('The number of vowels in the String %s is %d.' \
                      % (word, num_vowels(word)))
            case 4:
                print('Enter the String of characters you ' \
                      + 'want to print backwards: ', end = '')
                word = input()
                print('The String %s printed backwards is: ' % (word), end = '')
                print_backwards(word)
                print('')
            case 5:
                print('Enter a positive integer to find the max digit of: ', end ='')
                num = int(input())
                print('The max digit of the integer %d is %d.' % (num, max_digit(num)))
            case 6: 
                print('End!')
            case _:
                print('Invalid choice!')
        print('')

if __name__=="__main__":
    main()
