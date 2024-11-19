# Name: Ashton Tully tullyah@miamioh.edu
# Dr. Goodman
# Section: CSE 174 J
# Date: September 16 2024
"""This program encrypts the digits of a phone number."""

def get_phone_number():
    # Prompting the user with a message
    print('Enter a 10 digit phone number (e.g. 5131234567): ', \
          end = '')
    # Saving the given number inside a constant variable
    PHONE_NUM = int(input())
    # Splits up number by area, central, and station number
    area_code = int(PHONE_NUM / 10000000)
    central_office = int((PHONE_NUM / 10000) % 1000)
    station_number = int((PHONE_NUM / 1) % 10000)
    # prints and retuns number
    print('(%d) %d - %d' % (area_code, central_office, station_number))
    return area_code, central_office, station_number
# Encrypts the station number
def encrypt_station(station_number):
    """Encryps the first and last two digits by turning them into a char"""
    first_two_dig = chr((station_number // 100) + 33)
    last_two_dig = chr((station_number % 100) + 33)
    # returns encrypted digits
    return last_two_dig, first_two_dig
# Encrypts the first two parts of the phone number
def encrypt_rest_of_num(area_code, central_office):
    """Combines area code and central office number and then subtracts it
    the max int value"""
    encrypted_number = 99756473822 - ((area_code * 1000) + (central_office))
    # Prints and returns the encrpyted number
    print(encrypted_number)
    return encrypted_number
# Main method
def main():
    """Calls the other functions and gets encrypted nums from them"""
    area_code, central_office, station_number = get_phone_number()
    last_two_dig, first_two_dig =  encrypt_station(station_number)
    # Prints phone num with encrypted station number
    print('(%d) %d - ' % (area_code, central_office) +
         '%c%c' % (last_two_dig, first_two_dig))
    # encrypts rest of num
    encrypted_num = encrypt_rest_of_num(area_code, central_office)
    # prints final encrypted phone num
    print('%c%d%c' % (last_two_dig, encrypted_num, first_two_dig), end = '')
# Using the variable __name__
if __name__=="__main__":
    main()
