# Ashton Yully
# Dr. Goodman
# CSE 174
# 25 September 2024
# Copyright: 2024 Ashton Yully

""" Practicing with for loop and files. """

# Implements the color selection task
def color_selection():
    """Forces the user to select a correct color and counts attempts"""
    attempts = 0
    while True:
        attempts += 1
        choice = input("Please choose a color between Blue, Red, or Yellow: ")
        if choice == "Blue" or choice == "Red" or choice == "Yellow":
            break
    print(f"It took you {attempts} tries to choose either Blue, Red, or Yellow.")

# Handles the patient data recording task
def patient_data():
    """Records patient data and writes it to a file"""
    num_patients = int(input("How many patients of data do you want to record: "))
    with open("output.txt", "w") as file:
        for _ in range(num_patients):
            first_name = input("Enter the patient's first name: ")
            last_name = input("Enter the patient's last name: ")
            age = input("Enter the patient's age: ")
            heart_rate = input("Enter the patient's current heart rate: ")
            bmi = input("Enter the patient's BMI: ")
            temperature = input("Enter the patient's current temperature: ")
            
            file.write(f"{first_name}\n{last_name}\n{age}\n{heart_rate}\n{bmi}\n{temperature}\n")

# Generates and displays the Fibonacci sequence
def fibonacci():
    """Generates and displays the Fibonacci sequence"""
    n = int(input("How many numbers of the Fibonacci Sequence would you like to display: "))
    a, b = 0, 1
    for i in range(n):
        if i > 0:
            print(" ", end="")
        print(a, end="")
        a, b = b, a + b
    print()

# Main function to run the program
def main():
    color_selection()
    print()  # Empty line for spacing
    patient_data()
    print()  # Empty line for spacing
    fibonacci()

# Using the special variable __name__
if __name__ == "__main__":
    main()
