"""
@author: Ashton Tully
@professor: Dr. Goodman
@date: 10-16-2024
@assignment: Class Assignment 8a

This program calculates the factorial of a user-provided integer.
"""

def factorial():
    """
    Calculate the factorial of a given number.

    Args:
        None

    Returns:
        int: The factorial of the input number.
    """
    num = get_user_input()
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def get_user_input():
    """
    Prompt the user for an integer input and validate it.

    Args:
        None

    Returns:
        int: The validated integer input from the user.
    """
    while True:
        user_input = input("Enter an integer to calculate the factorial of: ")
        try:
            return extract_int(user_input)
        except ValueError:
            print("Error, you entered a non-integer input!")

def extract_int(input_string):
    """
    Convert a string to an integer.

    Args:
        input_string (str): The string to be converted to an integer.

    Returns:
        int: The integer value of the input string.
    """
    return int(input_string)

def main():
    result = factorial()
    print("The factorial is: " % result)

if __name__ == "__main__":
    main()
