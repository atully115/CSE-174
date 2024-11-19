#Author: Ashton Tully
#Dr. Goodman
#CSE 174
#Lab3
#Copyright: 2024 Ashton Tully
"""The purpose of this program is to calculate a person's BMI index"""

# Gets info from user
def get_info():
    """Prompts user to for their name, age, weight and height"""
    print("Enter your first and last name: ", end = '')
    name = input()
    print("Enter your age: ", end = '')
    age = int(input())
    print('Enter your weight(lb): ', end = '')
    weight = float(input())
    print('Enter your height(feet): ', end = '')
    height = float(input()) * 12
    # Calls print info fucntion
    print_info(name, age, weight, height)
    # returns necessary variables
    return name, age, weight, height
# Prints the bmi information in the correct format
def print_info(name, age, weight, height):
    """Calcs bmi"""
    bmi = ((weight * 703) / height) / height
    # Prints table
    print(' --------------------------------------')
    print('|%-20s|%-8s|%-8s|' % ('Name', 'Age', 'BMI'))
    print('|......................................|')
    print('|%-20s|%-8d|%-8.1f|' % (name, age, bmi))
    print(' --------------------------------------')
# Reads from a file and returns variables
def read_file():
    """Prompts user to enter the input file name"""
    print('Enter an input filename: ', end = '')
    fileName = input()
    # Opens file and reads it and assigns variables
    file = open(fileName,'r')
    name = file.readline().strip()
    age = int(file.readline())
    weight = float(file.readline())
    height = float(file.readline()) * 12
    # Calls print info function
    print_info(name, age, weight, height)
    # Closes file
    file.close()
    # returns necessary variables
    return name, age, weight, height
# Essentially main method v2. This calls the get info and read file
# functions and gets the necessary varaibles from them. It then
# creates and writes to a file.
def write_file():
    """Calls and gets variables from get info function"""
    name1, age1, weight1, height1 = get_info()
    # Calcs bmi
    bmi1 = ((weight1 * 703) / height1) / height1
    # Calls and gets variables from read file method
    name2, age2, weight2, height2 = read_file()
    bmi2 = ((weight2 * 703) / height2) / height2
    # Prompts user to enter output file name
    print('Enter an output filename: ', end = '')
    fileName = input()
    # Creates file and writes to it
    file = open(fileName, 'w')
    file.write(' --------------------------------------\n')
    file.write('|%-20s|%-8s|%-8s|\n' % ('Name', 'Age', 'BMI'))
    file.write('|......................................|\n')
    file.write('|%-20s|%-8d|%-8.1f|\n' % (name1, age1, bmi1))
    file.write('|......................................|\n')
    file.write('|%-20s|%-8d|%-8.1f|\n' % (name2, age2, bmi2))
    file.write(' --------------------------------------\n')
    # closes file
    file.close()
# Main Method
def main():
    """calls the write file fucntion"""
    write_file()
# using the special variable __name__
if __name__ == "__main__":
    main()
