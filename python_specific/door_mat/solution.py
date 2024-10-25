"""
Challenge: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
"""
import math

def print_door_mat(n, m):
    mat = []
    center_value = 'WELCOME'
    special_symbols = '.|.'
    special_symbols_count = 1
    single_char = '-'
    for i in range(n):
        if i+1 < math.ceil(n/2):
            middle_value = special_symbols * special_symbols_count
            special_symbols_count += 2
            len_single_char = int((m - len(middle_value)) / 2)
            row_val = (single_char * len_single_char) + middle_value + (single_char * len_single_char)
            mat.append(row_val)
        elif i+1 == math.ceil(n/2):
            len_single_char = int((m - len(center_value)) / 2)
            row_val = (single_char * len_single_char) + center_value + (single_char * len_single_char)
            mat.append(row_val)
            special_symbols_count -= 2
        else:
            middle_value = special_symbols * special_symbols_count
            special_symbols_count -= 2
            len_single_char = int((m - len(middle_value)) / 2)
            row_val = (single_char * len_single_char) + middle_value + (single_char * len_single_char)
            mat.append(row_val)
    
    for i in range(n):
        print(mat[i])
        


if __name__=='__main__':
    dimensions = input()
    n = int(dimensions.split(' ')[0])
    m = int(dimensions.split(' ')[1])

    print_door_mat(n, m)
