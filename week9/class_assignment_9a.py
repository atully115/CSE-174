# Author: Ashton Tully
# Professor: Dr. Goodman
# CSE 174 J
# Date: 10/23/2024
# Copyright: 2024 Ashton Tully
"""Purpose of this is to revist old concepts"""

def get_credits():
    """
    Determine the year based on the user's input.
    """
    while True:
        try:
            credits = int(input("Enter how many credit hours you have completed: "))
            if credits >= 0:  
                return credits
        except ValueError:
            print("Error, you did not enter an integer!")

def determine_year(credits):
    """
    Determine the year based on the user's input.
    """
    if credits >= 96:
        return "Senior"
    elif credits >= 64:
        return "Junior"
    elif credits >= 30:
        return "Sophomore"
    else:
        return "Freshman"
    
def print_table_headers(size):
    """Prints the division table headers"""
    print("\nDivision Table:")
    print(" ", end='\t\t')
    for i in range(1, size + 1):
        print("%d" % i, end='\t')
    print()

def print_table_row(row_num, size):
    """Prints a single row of the division table"""
    print("\t%d" % row_num, end='')
    for col in range(1, size + 1):
        result = row_num // col 
        print("\t%d" % result, end='')
    print()

def print_division_table(size):
    """Prints a complete division table of size x size"""
    print_table_headers(size)
    for row in range(1, size + 1):
        print_table_row(row, size)

def main():
    # Determine year status
    credits = get_credits()
    year = determine_year(credits)
    print("With %d hours completed, you have %s standing." % (credits, year))
    
    # Gets division table
    print_division_table(5)
      
if __name__ == "__main__":
    main()
