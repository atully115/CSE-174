# Ashton Tully
# Dr. Goodman
# 10/13/2024
# CSE 174 Section J
# Project 2
"""Polish Notation Calculator"""

def main():
    # Ask the user to input a file name
    file_name = input("Enter input file name: ")
    
    # Open the file for reading
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File '%s' not found." % file_name)
        return

    # Needed variables
    previous_result = 0
    line_number = 1

    # Goes through each line in the file
    for scan in lines:
        not_an_integer = False
        division_by_zero = False
        no_operator = False
        result = 0

        read = scan.split()
        if not read:  # Skip empty lines
            continue
        
        operator = read[0]  # Operator is already a string

        # if statements that have the operators needed and does the actions based on the operator
        if operator == "+":
            try:
                result = sum(int(x) for x in read[1:])
            except ValueError:
                not_an_integer = True
                previous_result = 0
        elif operator == "<+":
            try:
                result = previous_result
                for x in read[1:]:
                    result += int(x)
            except ValueError:
                not_an_integer = True
                previous_result = 0
        elif operator == "-":
            try:
                result = int(read[1])
                for x in read[2:]:
                    result -= int(x)
            except ValueError:
                not_an_integer = True
                previous_result = 0
        elif operator == "<-":
            try:
                result = previous_result
                for x in read[1:]:
                    result -= int(x)
            except ValueError:
                not_an_integer = True
                previous_result = 0
        elif operator == "*":
            try:
                result = 1
                for x in read[1:]:
                    result *= int(x)
            except ValueError:
                not_an_integer = True
                previous_result = 0
        elif operator == "<*":
            try:
                result = previous_result
                for x in read[1:]:
                    result *= int(x)
            except ValueError:
                not_an_integer = True
                previous_result = 0
        elif operator == "/":
            try:
                result = int(read[1])
                for x in read[2:]:
                    if int(x) == 0:
                        division_by_zero = True
                        previous_result = 0
                        break
                    result //= int(x)
            except ValueError:
                not_an_integer = True
                previous_result = 0
        elif operator == "</":
            try:
                result = previous_result
                if len(read) > 1 and int(read[1]) == 0:
                    division_by_zero = True
                    previous_result = 0
                elif len(read) > 1:
                    result //= int(read[1])
            except ValueError:
                not_an_integer = True
                previous_result = 0
        else:
            no_operator = True

        # Printing the appropriate results based on the booleans
        if no_operator:
            print("Result of Line %d: No operator %s" % (line_number, scan.strip()))
        elif division_by_zero:
            print("Result of Line %d: Error: / by zero" % line_number)
        elif not_an_integer:
            print("Result of Line %d: Non-integer input on this Line" % line_number)
        else:
            print("Result of Line %d: %d" % (line_number, result))
            previous_result = result  # Update previous_result for next iteration

        line_number += 1

if __name__ == "__main__":
    main()
