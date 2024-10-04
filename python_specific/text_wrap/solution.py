"""
Task link: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
"""

import textwrap

def wrap(string, max_width):
    last_index = 0
    final_index = len(string)
    wrapped_string = ''
    flag = True
    while flag:
        if last_index + max_width >= final_index:
            wrapped_string += string[last_index:final_index]
            break
        wrapped_string += string[last_index:last_index + max_width] + '\n'
        last_index += max_width
    return wrapped_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
