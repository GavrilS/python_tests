"""
Task: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
Mutate a string
"""

def mutate_string(string, position, character):
    mutable_value = list(string)
    mutable_value[position] = character
    return ''.join(mutable_value)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
