# Author: Ashton Tully
"""Computes the area of a trapazoid using two sets of values."""

# Calculates the are of the trapazoid
def main():
    """Calculates the are of the trapazoid"""
    long_base = 10
    short_base = 5
    altitude = long_base * short_base
    area = 0.0

    print('Long Base =' + str(long_base))
    print('Short Base =' + str(short_base))
    print('Altitude = ' + str(altitude))

    print("Adjusting Altitude to 9.")
    altitude = 9

    print('Long Base =' + str(long_base))
    print('Short Base =' + str(short_base))
    print('Altitude = ' + str(altitude))

    print('Area = ', end = '')
    area = (long_base + short_base) / 2 * altitude
    print(area)

# Using the variable __name__
if __name__=="__main__":
    main()
