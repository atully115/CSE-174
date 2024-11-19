# Ashton Tully
# Dr. Goodman
# CSE 174
# Class assignment
# September 18 2024
"""Practicing math operators and nest if statements"""

# Gets age and checks for eligibility for dirvers license
def drivers_license():
    """Gets age from user"""
    print('Enter your age: ', end= '')
    age = float(input())
    # Series of elif statements to check users age
    if (age >= 18):
        print("Do you have a learner's permit, yes or no: ", end = '')
        answer = input().lower()
        if (answer == 'yes'):
            print("You are eligible for a driver's license.")
        elif (answer == 'no'):
            print("You are eligible for a driver's license." +
                  " Please obtain a learner's permit first.")
    elif (age < 18 and age >= 15.5):
        print("You must obtain and have a learner's permit for 6 months.")
    else:
        print("You are not eligible for a driver's license.")   
# Simple calculator
def calculator():
    """Asks user for two numbers to calculate togethor"""
    print('\nEnter the first number: ', end = '')
    first_num = float(input())
    print('Enter the second number: ', end = '')
    second_num = float(input())
    # Asks user what opertation they want to choose
    print('Select and operation:\n1. Addition\n2. Subtraction\n' +
          '3. Multiplication\n4. Division')
    print('Enter either 1, 2, 3, or 4 for your choice: ', end = '')
    choice = input()
    result = 0
    # Elifs to perform correct calculation
    if (choice == '1'):
        result = first_num + second_num
    elif (choice == '2'):
        result = first_num - second_num
    elif (choice == '3'):
        result = first_num * second_num
    elif (choice == '4'):
        result = first_num / second_num
    print('Result: %.2f.' % (result))
# Main Function
def main():
    drivers_license()
    calculator()
    
# Test 1:
# 18
# nO
# 47.3
# 3
# 1

# Test 2:
# 15.5
# 47.3
# 3
# 2

# Test 3:
# 14
# 47.3
# 3
# 3

# Test 2:
# 25
# yEs
# 47.3
# 3
# 4
    
# Using the variable __name__
if __name__=="__main__":
    main()
