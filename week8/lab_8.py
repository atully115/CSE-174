# Author: Ashton Tully
# Professor: Dr. Goodman
# Date: 10/19/2024
# CSE 174
# Lab 8


def get_letter(binary_code: str) -> str:
    """
    Converts an 8-digit binary code to its corresponding ASCII character.

    Args:
    binary_code (str): An 8-digit binary code.

    Returns:
    str: The corresponding ASCII character, or an error message if input is invalid.
    """
    if len(binary_code) != 8 or not all(bit in '01' for bit in binary_code):
        return "Error: Invalid binary code. Please enter exactly 8 binary digits (0's and 1's)."
    
    ascii_value = 0
    for i in range(8):
        if binary_code[i] == '1':
            ascii_value += 2 ** (7 - i)
    return chr(ascii_value)

def get_word(binary_codes: str) -> str:
    """
    Converts a string of multiple 8-digit binary codes to a word.

    Args:
    binary_codes (str): A string containing multiple 8-digit binary codes.

    Returns:
    str: The corresponding word, or an error message if input is invalid.
    """
    if len(binary_codes) % 8 != 0 or not all(bit in '01' for bit in binary_codes):
        return "Error: Invalid binary codes. Please enter a sequence of 8-digit binary codes."
    
    word = ""
    for i in range(0, len(binary_codes), 8):
        binary_code = binary_codes[i:i+8]
        letter = get_letter(binary_code)
        if letter.startswith("Error"):
            return letter  # Propagate the error message
        word += letter
    return word

def menu() -> None:
    """
    Prints a menu with options on the display.

    Args: None
    Returns: None
    """
    print('**Binary Code Translator v 1.0**')
    print('1. Translate a binary code into a letter')
    print('2. Translate binary codes into a word')
    print('3. Exit\nEnter a number [1-3]: ', end='')

def process_option(option: int) -> bool:
    """
    Processes the user's menu option.

    Args:
    option (int): The user's selected option.

    Returns:
    bool: True if the program should continue, False if it should exit.
    """
    match option:
        case 1:
            print('Enter a single binary code: ', end='')
            letter = get_letter(input().strip())
            print('The letter is: %s\n' % (letter))
        case 2:
            print('Enter binary codes: ', end='')
            word = get_word(input().strip())
            print('The word is: %s\n' % (word))
        case 3:
            print('End!')
            return False
        case _:
            print('Invalid input!')
    return True

def main():
    """
    Runs the main loop of the Binary Code Translator program, displaying a menu and processing 
    the user's selected option.
    """
    continue_program = True
    while continue_program:
        menu()
        try:
            option = int(input())
        except ValueError:
            option = 0
        continue_program = process_option(option)

if __name__ == "__main__":
    main()
