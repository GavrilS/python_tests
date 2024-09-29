"""
Task: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
Find how many times a substring is present in a string.
"""

def count_substring(string, sub_string):
    counter = 0
    for index in range(0, len(string)):
        if string[index:].startswith(sub_string):
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
