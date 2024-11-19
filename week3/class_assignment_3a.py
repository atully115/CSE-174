#Author: Ashton Tully
#Dr. Goodman
#CSE 174
#Class assignment 3a
#Copyright: Ashton Tully 2024
"""Purpose of this program is to practice input(), output, and files"""

# fucntion for the ouput section of assignment
def output():
    """gets age, gpa, and name then prints with format"""
    age = 5
    print('The age is:%5d'%(age))
    gpa = 3.42342
    print('The gpa is: %.2f'%(gpa))
    name = 'Garret'
    print('The name is: %-25s'%(name))
    print('The age is%5d, The gpa is %.2f,' % (age, gpa) +
          ' is %-25s' % (name))
# function to get the user input part of the assignment
def user_input():
    """Gets the user's first and last name and then their exam scores"""
    print('Enter the first name: ',end='')
    first = input()
    print('Enter the last name: ',end='')
    last = input()
    print('Enter three exam grades seperately by pressing' +
          'enter after each grade:')
    first_grade = float(input())
    second_grade = float(input())
    third_grade = float(input())
    # calculates the average and prints it in a formatted way
    avg = (first_grade + second_grade + third_grade) / 3
    print('The average grade of %s %s is:  %.2f' % (first, last, avg))
# Function for the read/write to a file
def to_file():
    """opens and reads the file"""
    file = open('data.txt','r')
    # assigns values for the first person
    name1 = file.readline()
    grade1 = float(file.readline())
    grade2 = float(file.readline())
    grade3 = float(file.readline())
    grade4 = float(file.readline())
    # assigns values for the second person
    name2 = file.readline()
    grade5 = float(file.readline())
    grade6 = float(file.readline())
    grade7 = float(file.readline())
    grade8 = float(file.readline())
    # assigns values for the third person
    name3 = file.readline()
    grade9 = float(file.readline())
    grade10 = float(file.readline())
    grade11 = float(file.readline())
    grade12 = float(file.readline())
    # creates a new file to write to
    file2 = open('output.txt','a')
    file2.write("The student's name is %s and their average " % (name1))
    file2.write("grade is %.2f.\n" % ((grade1 + grade2 + grade3 + grade4) / 4))  
    file2.write("The student's name is %s and their average " % (name2))
    file2.write("grade is %.2f\n" % ((grade5 + grade6 + grade7 + grade8) / 4))
    file2.write("The student's name is %s and their average " % (name3))
    file2.write("grade is %.2f\n" % ((grade9 + grade10 + grade11 + grade12) / 4))
    
# main method
def main():
    """This is the main method"""
    output()
    user_input()
    to_file()
    
#    using the special variable __name__
if __name__=="__main__":
    main()
