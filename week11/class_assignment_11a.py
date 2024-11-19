# Author: Ashton Tully
# Dr. Goodman
# CSE 174 J
# 11/06/2024
"""Purpose is to practice 2D lists"""

import random

def create_2D(rows, cols):
    nums = []
    for _ in range(rows):
        row = [random.random() * 100 for _ in range(cols)]
        nums.append(row)
    return nums

def display(nums):
    for row in nums:
        print(" ".join("%.2f" % value for value in row))
        
def max_2D(nums):
    max_value = nums[0][0]
    for row in nums:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value

def min_2D(nums):
    min_value = nums[0][0]
    for row in nums:
        for value in row:
            if value < min_value:
                min_value = value
    return min_value

def mean_2D(nums):
    total = 0
    count = 0
    for row in nums:
        for value in row:
            total += value
            count += 1
    return total / count
def main():
    nums = create_2D(3, 5)
    display(nums)
    
    print("\nMaximum value of the 2D list: %.2f." % max_2D(nums))
    print("Minimum value of the 2D list: %.2f." % min_2D(nums))
    print("Mean value of the 2D list: %.2f." % mean_2D(nums))
    

if __name__ == "__main__":
    main()