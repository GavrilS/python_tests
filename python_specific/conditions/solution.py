"""
Task: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
"""

def check_condition(n):
    if n % 2 != 0:
        print('Weird')
    else:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        elif n > 20:
            print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    check_condition(n)
