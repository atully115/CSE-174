# Author: Ashton Tully
# Dr. Goodman
# CSE 174
# 09/28/2024
# Lab 5
""" The program reads a file containing student grades, 
and outputs a file containing the letter grades.
"""
#  Function to process grades
def process_grades(input_file, output_file):
    """Processes grades from an input file, writes the 
    letter grades to an output file, and calculates 
    and displays the average score.
    """
    total_score = 0
    student_count = 0

    for line in input_file:
        # Split the line into words
        words = line.strip().split()
    
        # Skip the first word (name) and process the rest
        is_first_word = True
        for word in words:
            if is_first_word:
                is_first_word = False
                continue
        
            if word.isdigit():
                score = int(word)
            
                # Determine letter grade
                if score >= 90:
                    grade = 'A'
                elif score >= 80:
                    grade = 'B'
                elif score >= 70:
                    grade = 'C'
                elif score >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
            
                # Write result to output file
                output_file.write("%s\n" % grade)
            
                # Add to total score and increment student count
                total_score += score
                student_count += 1
    return total_score, student_count
# Function to calculate the average score
def calculate_average(total_score, student_count):
    """
    Calculates the average score given the total score and
    the number of students.
    """
    return total_score / student_count if student_count > 0 else 0
# Function to display the results
def display_results(student_count, average_score):
    """Displays the number of students and the average score"""
    print("Number of students: %d" % student_count)
    print("Class average: %.2f" % average_score, end='')
# Function to write the results to the output file
def write_results(output_file, student_count, average_score):
    """Writes the number of students and the average score to
    the output file"""
    output_file.write("Number of students: %d\n" % student_count)
    output_file.write("Class average: %.2f\n" % average_score)
# Main function to run the program
def main():
    """Main function to run the program"""
    # Get input filename from user and open the file
    input_filename = input("Enter an input file name: ")
    input_file = open(input_filename, 'r')

    # Get output filename from user and open the file
    output_filename = input("Enter an output file name: ")
    output_file = open(output_filename, 'w')

    # Process grades
    total_score, student_count = process_grades(input_file, output_file)

    # Calculate average
    average_score = calculate_average(total_score, student_count)

    # Display results in console
    display_results(student_count, average_score)

    # Write results to output file
    write_results(output_file, student_count, average_score)

    # Close files
    input_file.close()
    output_file.close()
    
# Run the program
if __name__ == "__main__":
    main()
