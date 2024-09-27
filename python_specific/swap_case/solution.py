"""
Task: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
"""

def swap_case(s):
    # swapped_string = s.swapcase()
    swapped_string = []
    for char in s:
        if char.isupper():
            swapped_string.append(char.lower())
        else:
            swapped_string.append(char.upper())
    return ''.join(swapped_string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
