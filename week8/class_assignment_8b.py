"""
@author: Ashton Tully
@professor: Dr. Goodman
@date: 10-16-2024
@assignment: Class Assignment 8b

Geometric area calculations and checking account functions.
Includes circle, rectangle, triangle area, and deposit.
"""

import math

checking = 0.0

def circle_area(radius=1.75):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle. Default is 1.75.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius**2

def rectangle_area(length, width=2.22):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle. Default is 2.22.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def triangle_area(base=5, height=5):
    """
    Calculate the area of a triangle.

    Args:
        base (float): The base of the triangle. Default is 5.
        height (float): The height of the triangle. Default is 5.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * base * height

def deposit(amount):
    """
    Deposit money into the checking account.

    Args:
        amount (float): The amount to deposit.
    """

import math

checking = 0.0

def circle_area(radius=1.75):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle. Default is 1.75.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius**2

def rectangle_area(length, width=2.22):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle. Default is 2.22.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def triangle_area(base=5, height=5):
    """
    Calculate the area of a triangle.

    Args:
        base (float): The base of the triangle. Default is 5.
        height (float): The height of the triangle. Default is 5.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * base * height

def deposit(amount):
    """
    Deposit money into the checking account.

    Args:
        amount (float): The amount to deposit.

    Side effects:
        Updates the global checking balance.
        Prints a message if the balance is still negative after deposit.
    """
    global checking
    checking += amount
    if checking < 0:
        print("You still have a negative balance after your deposit!")

def withdraw(amount):
    """
    Withdraw money from the checking account.

    Args:
        amount (float): The amount to withdraw.

    Side effects:
        Updates the global checking balance.
        Prints a message if the balance becomes negative after withdrawal.
    """
    global checking
    if checking - amount < 0:
        print("You have a negative balance after your withdrawal!")
    checking -= amount

def main():
    """
    Main function to test geometry and bank account functions.

    This function demonstrates the usage of various geometry functions
    (circle_area, rectangle_area, triangle_area) and bank account functions
    (withdraw, deposit) with different arguments and prints the results.
    """
    # Testing geometry functions
    print("The area of a circle given the radius 22.5 = %.2f." % circle_area(22.5))
    print("The area of a rectangle given the length and width of 15.5 and 17.7 = %.2f." % rectangle_area(15.5, 17.7))
    print("The area of a triangle given the base and height of 5 and 6 = %.2f." % triangle_area(5, 6))
    print("The circle's area with no argument is %.2f." % circle_area())
    print("The rectangle's area using positional arguments is %.2f." % rectangle_area(13.37))
    print("The triangle's area using keyword arguments is %.2f." % triangle_area(height=21, base=17))
    print()

    # Testing bank account functions
    withdraw(100)
    print("Checking balance after withdrawing $100.00: $%.2f." % checking)
    deposit(50)
    print("Checking balance after depositing $50.00: $%.2f." % checking)
    deposit(150)
    print("Checking balance after depositing $150.00: $%.2f." % checking)
    deposit(25)
    print("Checking balance after depositing $25.00: $%.2f." % checking)
    withdraw(100)
    print("Checking balance after withdrawing $100.00: $%.2f." % checking)

if __name__ == "__main__":
    main()
