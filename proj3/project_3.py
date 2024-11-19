# @author Dr. Garrett Goodman
# Starter code for Project 3.
# Modified by Ashton Tully
# Dr Goodman
# CSE 174 J
# Project 3
# 11/1/2024
"""Project Three"""

def not_descending(a: int, b: int, c: int) -> bool:
    """
    Checks if three integers are in descending order.

    Args:
        a (int): First integer.
        b (int): Second integer.
        c (int): Third integer.

    Returns:
        bool: True if integers are in descending order, False otherwise.
    """
    if a > b and b > c:
        return True
    return False

def check_nums(n: int, start: int, end: int, check: bool) -> bool:
    """
    Checks if a number is within or outside a range.

    Args:
        n (int): The number to check.
        start (int): Range start.
        end (int): Range end.
        check (bool): True to check within range, False for outside.

    Returns:
        bool: True if condition is met, False otherwise.
    """
    if check:
        return start <= n <= end
    return n < start or n > end

def get_substring(inp: str, start: int, end: int, check: bool) -> str:
    """
    Extracts a substring.

    Args:
        inp (str): Input string.
        start (int): Start index.
        end (int): End index if `check` is True.
        check (bool): If True, uses [start, end); if False, [start, end of string).

    Returns:
        str: The extracted substring.
    """
    if check:
        return inp[start:end]
    return inp[start:]

def switch_xo(inp: str) -> str:
    """
    Swaps 'X' and 'O' in a string.

    Args:
        inp (str): Input string.

    Returns:
        str: String with 'X' and 'O' swapped.
    """
    result = ''
    for char in inp:
        if char == 'X':
            result += 'O'
        elif char == 'O':
            result += 'X'
        else:
            result += char
    return result

def next_div7(num: int) -> int:
    """
    Finds the next number divisible by 7.

    Args:
        num (int): Starting number.

    Returns:
        int: The next number divisible by 7.
    """
    current = num + 1
    while current % 7 != 0:
        current += 1
    return current

def change_odd_chars(inp: str, odd: bool) -> str:
    """
    Capitalizes characters at odd indices.

    Args:
        inp (str): Input string.
        odd (bool): If True, modifies odd-index characters.

    Returns:
        str: Modified string with uppercase at odd indices.
    """
    inp = inp.lower()
    for i in range(len(inp)):
        if i % 2 == 1:
            inp = inp[:i] + inp[i].upper() + inp[i+1:]
    return inp

def what_missing(inp: str) -> str:
    """
    Finds the missing character in a sequence.

    Args:
        inp (str): Alphabetical string sequence.

    Returns:
        str: Missing character, or empty if none.
    """
    for i in range(1, len(inp)):
        if ord(inp[i]) != ord(inp[i-1]) + 1:
            return chr(ord(inp[i-1]) + 1)
    return ''

def get_similars(s1: str, s2: str, s3: str) -> str:
    """
    Finds common characters at the same index in three strings.

    Args:
        s1 (str): First string.
        s2 (str): Second string.
        s3 (str): Third string.

    Returns:
        str: Common characters at matching indices.
    """
    result = ''
    min_len = min(len(s1), len(s2), len(s3))
    for i in range(min_len):
        if s1[i] == s2[i] == s3[i]:
            result += s1[i]
    return result

def add_digits(inp: str) -> int:
    """
    Sums digit characters in a string.

    Args:
        inp (str): Input string.

    Returns:
        int: Sum of digits in the string.
    """
    result = 0
    for char in inp:
        if char.isdigit():
            result += int(char)
    return result

def add_divisibles(num: int) -> int:
    """
    Sums even divisors of a number.

    Args:
        num (int): The number to check divisors.

    Returns:
        int: Sum of even divisors.
    """
    result = 0  
    for i in range(1, num):
        if num % i == 0 and i % 2 == 0:
            result += i
    return result

def fix_sentence(inp: str) -> str:
    """
    Capitalizes the start of each word.

    Args:
        inp (str): Input string.

    Returns:
        str: Sentence with capitalized words.
    """
    for i in range(len(inp)):
        if i == 0 or inp[i-1] == ' ':
            inp = inp[:i] + inp[i].upper() + inp[i+1:]
    return inp

def switch_signs(inp: str) -> str:
    """
    Switches signs of space-separated numbers.

    Args:
        inp (str): String of numbers.

    Returns:
        str: String with sign of each number switched.
    """
    numbers = inp.split()
    result = []
    for num in numbers:
        if num.startswith('-'):
            result.append(num[1:])
        else:
            result.append('-' + num)
    return ' '.join(result)

def double_hi(inp: str) -> bool:
    """
    Checks for two consecutive "hi" sequences.

    Args:
        inp (str): Input string.

    Returns:
        bool: True if two consecutive "hi" sequences are found.
    """
    hcount = 0
    icount = 0
    for char in inp:
        if hcount < icount:
            icount = 0
        if char.lower() == 'h':
            hcount += 1
        elif char.lower() == 'i':
            icount += 1
        if hcount == 2 and icount == 2:
            return True
    return False

def put_together(inp: str) -> str:
    """
    Combines repeating sequences into single occurrences.

    Args:
        inp (str): Input string.

    Returns:
        str: String with reduced repeated sequences.
    """
    result = ""
    for i in range(len(inp)):
        if i > 0 and inp[i] in result:
            continue
        current = inp[i]
        for j in range(i + 1, len(inp)):
            if inp[j] == current[0]:
                current += inp[j]
        result += current
    return result

def get_sec_max(inp: str) -> float:
    """
    Finds the second largest number in a string.

    Args:
        inp (str): String of numbers.

    Returns:
        float: Second largest number, or 0.0 if empty.
    """
    if str(inp) == '':
        return 0.0
    else:
        numbers = inp.split()
        numbers.sort(reverse=True)
        return float(numbers[1])

def main():
    print('***Testing not_descending***')
    print('False == ' + str(not_descending(1, 2, 3)))
    print('True == ' + str(not_descending(3, 2, 1)))
    print('True == ' + str(not_descending(-2, -3, -4)))
    print('')

    print('***Testing check_nums***')
    print('True == ' + str(check_nums(2, 1, 10, True)))
    print('False == ' + str(check_nums(0, 1, 10, True)))
    print('True == ' + str(check_nums(10, 9, 10, True)))
    print('')

    print('***Testing get_substring***')
    print('a == ' + str(get_substring('abc', 0, 1, True)))
    print('000111222 == ' + str(get_substring('000111222', 0, 3, False)))
    print('Hell == ' + str(get_substring('Hello', 0, 4, True)))
    print('')

    print('***Testing switch_xo***')
    print('O == ' + str(switch_xo('X')))
    print(' == ' + str(switch_xo('')))
    print('XO == ' + str(switch_xo('OX')))
    print('')

    print('***Testing next_div7***')
    print('7 == ' + str(next_div7(1)))
    print('14 == ' + str(next_div7(8)))
    print('14 == ' + str(next_div7(9)))
    print('')

    print('***Testing change_odd_chars***')
    print('aB == ' + str(change_odd_chars('ab', True)))
    print('aAaAa == ' + str(change_odd_chars('aaaaa', True)))
    print('aBcSdE == ' + str(change_odd_chars('ABcsde', True)))
    print('')

    print('***Testing what_missing***')
    print('b == ' + str(what_missing('ac')))
    print(' == ' + str(what_missing('ab')))
    print('f == ' + str(what_missing('abcdeg')))
    print('')

    print('***Testing get_similars***')
    print('ab == ' + str(get_similars('ab', 'ab', 'ab')))
    print('a == ' + str(get_similars('ab', 'ac', 'ad')))
    print('a == ' + str(get_similars('a', 'ab', 'abc')))
    print('')

    print('***Testing add_digits***')
    print('0 == ' + str(add_digits('')))
    print('0 == ' + str(add_digits('a0')))
    print('3 == ' + str(add_digits('1fr2')))
    print('')

    print('***Testing add_divisibles***')
    print('12 == ' + str(add_divisibles(12)))
    print('0 == ' + str(add_divisibles(1)))
    print('0 == ' + str(add_divisibles(5)))
    print('')

    print('***Testing fix_sentence***')
    print('Hi == ' + str(fix_sentence('hi')))
    print('Good Morning == ' + str(fix_sentence('Good morning')))
    print('Nice Job! == ' + str(fix_sentence('nice job!')))
    print('')

    print('***Testing switch_signs***')
    print(' == ' + str(switch_signs('')))
    print('-1 == ' + str(switch_signs('1')))
    print('2 -3 == ' + str(switch_signs('-2 3')))
    print('')

    print('***Testing double_hi***')
    print('True == ' + str(double_hi('HiHi')))
    print('False == ' + str(double_hi('')))
    print('True == ' + str(double_hi('Hkji3Hi')))
    print('')

    print('***Testing put_together***')
    print(' == ' + str(put_together('')))
    print('aacd == ' + str(put_together('acda')))
    print('11ww222gddm == ' + str(put_together('1w2g1dw2md2')))
    print('')

    print('***Testing get_sec_max***')
    print('1.2 == ' + str(get_sec_max('2 1.2')))
    print('4.1 == ' + str(get_sec_max('1.3 4.1 5')))
    print('0.0 == ' + str(get_sec_max('')), end='')

if __name__=="__main__":
    main()