# Author: Ashton Tully
# Professor: Dr. Goodman
# CSE 174 J
# Date: 10/30/2024
# Copyright: 2024 Ashton Tully
"""Purpose of this is to practice List"""

def display(lst):
    """Print each value in the list on a new line"""
    for item in lst:
        print(item)

def get_index_and_value(prompt_number):
    """Get index and value from user input"""
    index = int(input("Enter the %s index to update between 0 and 9: " % prompt_number))
    value = int(input("Enter the value to change index %d to: " % index))
    return index, value

def update_list_values(numbers):
    """Update three indices in the list based on user input"""
    # Get three sets of indices and values
    prompts = ['first', 'second', 'third']
    updates = []
    
    for prompt in prompts:
        index, value = get_index_and_value(prompt)
        numbers[index] = value
        updates.append((index, value))
    
    # Print confirmation message
    print("Indices %d, %d, and %d have been changed to the values of %d, %d, and %d, respectively." % 
          (updates[0][0], updates[1][0], updates[2][0], 
           updates[0][1], updates[1][1], updates[2][1]))
    
    return numbers

def check_odd_even(numbers):
    """Check if value at user-specified index is odd or even"""
    index = int(input("Enter an index between 0 and 9 to see if the value is negative or positive: "))
    value = numbers[index]
    if value % 2 == 0:
        print("The value %d at index %d is even." % (value, index))
    else:
        print("The value %d at index %d is odd." % (value, index))

def display_range(numbers):
    """Display values in user-specified range"""
    print("Enter two values between 0 and 9 to form a range to display values in the list:")
    start = int(input())
    end = int(input())
    
    for i in range(start, end + 1):
        print(numbers[i], end=" ")
    print()

def calculate_even_string_lengths(string_list):
    """Calculate sum of even-length strings in list"""
    return sum(len(s) for s in string_list if len(s) % 2 == 0)

def main():
    # Initialize lists
    numbers = list(range(1, 11))
    mixed_list = ['I am a String', 22, True, 97.5]
    string_list = ['Hello', 'Hi', 'CSE 174!']
    
    # Display mixed list
    display(mixed_list)
    
    # Update list values
    numbers = update_list_values(numbers)
    
    # Check if value is odd/even
    check_odd_even(numbers)
    
    # Display range of values
    display_range(numbers)
    
    # Display final string list and sum
    print("\nWith the list:")
    print(string_list)
    even_sum = calculate_even_string_lengths(string_list)
    print("The sum of the even lengths of all strings in the list is %d." % even_sum)

if __name__ == "__main__":
    main()