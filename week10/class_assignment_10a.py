# Author: Ashton Tully
# Professor: Dr. Goodman
# CSE 174 J
# Date: 10/30/2024
# Copyright: 2024 Ashton Tully
"""Purpose of this is to practice recursion"""

def multiply_greater4(n:int):
    return multiply_helper4(n, 0)

def multiply_helper4(n:int, result:int):
    if n == 0:
        return result
    digit = n % 10
    if digit > 4:
            if result > 0:
                return multiply_helper4(n // 10, result * digit)
            else:
                return multiply_helper4(n // 10, digit)
    return multiply_helper4(n // 10, result)

def remove_cse(word: str):
    return remove_helper(word, "")

def remove_helper(word: str, result: str):
    if len(word) < 3:
        return result + word
    if word[:3].lower() == "cse":
        return remove_helper(word[3:], result)
    return remove_helper(word[1:], result + word[0])

def main():
    print("Testing multiply_greater4():")
    print(multiply_greater4(337546192))
    print(multiply_greater4(36))
    print(multiply_greater4(44587))
    print()
    print("Testing remove_cse():")
    print(remove_cse("hicsehello"))
    print(remove_cse("csecsecse"))
    print(remove_cse("i love cse 174"))
    
if __name__ == "__main__":
    main()
