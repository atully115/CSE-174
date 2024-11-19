#Author: Ashton Tully
#Dr. Goodman
#CSE 174
#Class assignment 3b
#Copyright: Ashton Tully 2024
"""Practice using elif statements"""
# function to determine voter age
def voter_eligibil():
    """Asks user for their age and takes in user input"""
    print('Please enter your age: ', end='')
    age = float(input())
    # checks voter age
    if (age >= 18):
        print("You are eligible to vote.\n")
    else:
        print("You are not eligible to vote yet.\n")
   
# function to help diagnosis a medical problem 
def medical_diagnosis():
    """Asks questions an takes in an input from user"""
    print("Do you have a fever, yes or no: ", end = '')
    fever = input().lower()
    print("Do you have a cough, yes or no: ", end ='')
    cough = input().lower()
    print('Do you have a headache, yes or no: ', end ='')
    headache = input().lower()
    # elif statements to determine diagnosis
    if (fever == 'yes' and cough == 'yes'):
        print('You may have the flu.\n')
    elif (headache == 'yes' and fever == 'no'):
        print('You may have a tension headache.\n')
    else:
        print("No specific diagnosis can be made.\n")
# function for the video game section
def video_game():
    """Prompts user with options"""
    print('You are facing a fearsome drage, what do you do?')
    print('1. Attack the dragon.\n2. Run away')
    print('3. Try to negotiate with the dragon.')
    # Creating bool variables
    choice = float(input())
    option1 = False
    option2 = False
    option3 = False
    # Start of elif statements
    if (choice == 1):
        option1 = True
    elif (choice == 2):
        option2 = True
    elif (choice == 3):
        option3 = True
    else:
        print('That is not an option!')
    # Start of second elif statements
    if (option1 == True):
        print('You bravely attack the dragon and defeat it!')
    elif (option2 == True):
        print('You run away from the dragon. Safety first!')
    elif (option3 == True):
        print("You attempt to negotiate with the dragon")
        print('It accepts your offer to treasure and spares you!')
# main method
def main():
    """This is the main method"""
    voter_eligibil()
    medical_diagnosis()
    video_game()

#    using the special variable __name__
if __name__=="__main__":
    main()