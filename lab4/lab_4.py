# Ashton Yully
# Dr. Goodman
# CSE 174 
# 21 September 2024
# Copyright: 2024 Ashton Tully
"""This program asks user to select a menu option and the executes
the desired option for the user"""

import math

# Menu screen
def menu():
    """Asks user to select a menu option and then returns that input back
    in to the main method"""
    print('Welcome to the problem solver!\nPlease choose one of the 4 ' +
          ' available options and follow all given prompts.')
    print("1. Determining a Student's Final Grade")
    print('2. Trigonometry Circle Quadrants')
    print('3. Getting Candy for Math')
    print('4. Solving a Summation Problem')
    return input()
# Determining a Student's Final Grade
def final_grade():
    """Asks for user to input a final grade"""
    print('Enter the final grade value: ', end = '')
    grade = float(input())
    # Uses elifs to find the grade of which that grade is and prints grade
    if (grade >= 90 and grade <= 100):
        print('The final grade is an A.')
    elif (grade >= 80 and grade <= 89.9):
        print('The final grade is an B.')
    elif (grade >= 70 and grade <= 79.9):
        print('The final grade is an C.')
    elif (grade >= 60 and grade <= 69.9):
        print('The final grade is an D.')
    elif (grade >= 0 and grade <= 59.9):
        print('The final grade is an F.')
# Trigonometry Circle Quadrants
def trigonometry():
    """Asks user for the degree of circle and the decides what quadrant
    it is in"""
    print('Enter the degree of the circle: ', end = '')
    degree = float(input())
    # Used for when degree is not in a quadrant using or statements
    if (degree == 0 or degree == 90 or degree == 180 or degree == 270
        or degree == 360):
        print('There is no quadrant.')
    # elifs to find the quadrant
    elif (degree >= 1 and degree <= 89):
        print('The degree %.2f is in Quadrant 1.' % (degree))
    elif (degree >= 91 and degree <= 179):
        print('The degree %.2f is in Quadrant 2.' % (degree))
    elif (degree >= 181 and degree <= 269):
        print('The degree %.2f is in Quadrant 3.' % (degree))
    elif (degree >= 271 and degree <= 359):
        print('The degree %.2f is in Quadrant 4.' % (degree))
# Getting Candy for Math
def candy():
    """Asks user for input and then uses math.sqrt() and math.pow()
    to check if the input is a perfect square"""
    print("Enter the number to see if it's a perfect square: ", end = '')
    x = int(input())
    y = math.sqrt(x)
    z = math.pow(y,2)
    # Prints true or false depending on results
    if (z == x):
        print('True')
    else:
        print('False')
# Solving a summation problem
def summation():
    """Asks the user for start and end points and uses a for loop to
    complete the summation sequence"""
    print('Enter the summation starting point: ', end = '')
    start = int(input())
    print('Enter the summation ending point: ', end = '')
    end_sum = int(input())
    summation = 0
    for i in range(start, end_sum + 1):
        summation += i
    print('The result of the summation is: %d' % summation)
# Main fucntion
def main():
    """Calls the menu functiona nd the goes through elif statements
    to find correct selection"""
    selection = menu()
    if (selection == '1'):
        final_grade()
    elif (selection == '2'):
        trigonometry()
    elif (selection == '3'):
        candy()
    elif (selection == '4'):
        summation()
#    using the special variable __name__
if __name__=="__main__":
    main()
