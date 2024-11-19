# Author: Ashton Tully
# Dr. Goodman
# CSE 174 J
# 11/06/2024
"""Purpose is to practice 2D lists"""

def main():
    list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_two = list_one
    list_one[4] = 57
    
    display(list_one)
    display(list_two)
    
    list_three = list_one[:]
    list_one[5] = 117
    
    display(list_one)
    display(list_three)
    
    list_four = [10, 2, 4, 10, 5, 6, 10, 10, -56, -33]
    
    first_ten = True
    i = 0

    while i < len(list_four):
        if list_four[i] == 10:
            if first_ten:
                first_ten = False
                i += 1
            else:
                list_four.pop(i)
        else:
            i += 1
                
    display(list_four)
    
    list_four.insert(0, 67)
    list_four.append(67)
    display(list_four)

def display(lst):
    print(" ".join(str(value) for value in lst))

if __name__ == "__main__":
    main()
