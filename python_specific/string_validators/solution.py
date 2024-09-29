"""
Task: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
Find if a string contains alphanumeric chars, alphabetical chars, digits, lowercase and 
uppercase characters.
"""

def validate_string(s):
    alnum = False
    alpha = False
    digits = False
    lower = False
    upper = False
    confirmed_checks = 0

    for char in s:
        if not alnum and char.isalnum():
            alnum = True
            confirmed_checks += 1
        
        if not alpha and char.isalpha():
            alpha = True
            confirmed_checks += 1
        
        if not digits and char.isdigit():
            digits = True
            confirmed_checks += 1
        
        if not lower and char.islower():
            lower = True
            confirmed_checks += 1
        
        if not upper and char.isupper():
            upper = True
            confirmed_checks += 1
        
        if confirmed_checks >= 5:
            break
    
    print(f"{alnum}\n{alpha}\n{digits}\n{lower}\n{upper}")


if __name__ == '__main__':
    s = input()
    validate_string(s)
