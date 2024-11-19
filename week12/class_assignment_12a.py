# Author: Ashton Tully
# Dr. Goodman
# 11/13/2024
# CSE 174 J
"""Practicing with lists and searching algorithms"""
def linear_search_2d(list, target):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == target:
                return [i, j]
    return [-1, -1]
def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
def main():
    list1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    print('Searching for 15 in the list with linear search, it is at index ', 
          linear_search(list1, 15))
    print('Searching for 15 in the list with linear search, it is at index ',
          linear_search(list1, 72))
    
    list2 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    print('Searching for 16 in the list with binary search, it is at index ',
          binary_search(list2, 16))
    print('Searching for 72 in the list with binary search, it is at index ',
          binary_search(list2, 72))
    list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('Searching for 6 in the 2d-list with linear search, it is at index ',
          linear_search_2d(list3, 5))
    print('Searching for 20 in the 2d-list with linear search, it is at index ',
          linear_search_2d(list3, 20))
    
if __name__ == "__main__":
    main()