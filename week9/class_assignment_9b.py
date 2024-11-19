# Author: Ashton Tully
# Professor: Dr. Goodman
# CSE 174 J
# Date: 10/23/2024
# Copyright: 2024 Ashton Tully
"""Purpose of this is to practice recursion"""

def sub_digits(n: int) -> int:
    if(n == 0):
       return 0
    return (n % 10) - sub_digits(n // 10)

def add_div3_digits(n: int) -> int:
   if n == 0:
       return 0
   
   current_digit = n % 10
   if current_digit % 3 == 0:
       return current_digit + add_div3_digits(n // 10)
   return add_div3_digits(n // 10)

def count_hi(s: str) -> int:
   if len(s) < 2:
       return 0
   
   if s[0:2] == 'hi':
       return 1 + count_hi(s[2:])
   
   return count_hi(s[1:])

def main():
   """
   Call stack for sub_digits(45224):
   1. sub_digits(45224) = 4 - sub_digits(4522)
   2. sub_digits(4522) = 2 - sub_digits(452)
   3. sub_digits(452) = 2 - sub_digits(45)
   4. sub_digits(45) = 5 - sub_digits(4)
   5. sub_digits(4) = 4 - sub_digits(0)
   6. sub_digits(0) = 0
   
   Then the function starts returning:
   6. returns 0
   5. 4 - 0 = 4
   4. 5 - 4 = 1
   3. 2 - 1 = 1
   2. 2 - 1 = 1
   1. 4 - 1 = 3
   Final result: 3
   """
   
   
   print("Testing sub_digits(45224):")
   print(sub_digits(45224))
   
   print("\nTesting add_div3_digits():")
   print(add_div3_digits(337546192))
   print(add_div3_digits(36))
   print(add_div3_digits(22587))
   
   print("\nTesting count_hi():")
   print(count_hi('hi'))
   print(count_hi('hello'))
   print(count_hi('hihellohi'))

if __name__ == "__main__":
    main()
