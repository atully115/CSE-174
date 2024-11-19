# Ashton Tully
# Dr. Goodman
# CSE 174
# 25 September 2024
# Copyright: 2024 Ashton Tully

""" Practice working with general loop problems and nested loops """

# Counts instances of "the" in a sentence
def count_the():
    """Counts the number of times 'the' appears in a sentence"""
    sentence = input("Enter a sentence to count the instances of the word \"the\". \n")
    count = sentence.lower().split().count("the")
    print(f'The number of "the" instances in the sentence are: {count}')
    print()

# Calculates factorial of a non-negative integer
def calculate_factorial():
    """Calculates the factorial of a non-negative integer"""
    while True:
        try:
            n = int(input("Please enter a non-negative integer to calculate the factorial: "))
            if n < 0:
                print("Error, please enter a non-negative integer: ", end="")
            else:
                result = 1
                for i in range(1, n + 1):
                    result *= i
                print(f"The factorial of {n} is {result}.")
                print()
                break
        except ValueError:
            print("Error, please enter a non-negative integer: ", end="")

# Prints a triangle pattern of X's
def print_triangle():
    """Prints a triangle pattern of X's based on user input"""
    size = int(input("Enter an integer between 1 and 10 to print a triangle of X's: "))
    while True:
            size = int(input("Enter an integer between 1 and 10 to print a triangle of X's: "))
            if 1 <= size <= 10:
                for i in range(1, size + 1):
                    print("X" * i)
                break
            else:
                print("Error, please enter an integer between 1 and 10: ", end="")

# Main function to run the program
def main():
    """Main function to execute all parts of the program"""
    count_the()
    calculate_factorial()
    print_triangle()

# Using the special variable __name__
if __name__ == "__main__":
    main()
