"""
Task: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']

def minion_game(string):
    pass


def check_player_score(type, string):
    flag = True
    score = 0
    words = []
    sub_string = ''
    word_length = 0
    last_index = 0
    while flag:
        for i in range(last_index, len(string)):
            if sub_string == '':
                if type == 'vowel':
                    if string[i].lower() in VOWELS:
                        sub_string = string[i]
                        score += 1
                        word_length += 1
                        words.append(sub_string)
                    else:
                        continue
                else:
                    if string[i].lower() in VOWELS:
                        continue
                    else:
                        sub_string = string[i]
                        score += 1
                        word_length += 1
                        words.append(sub_string)
            else:
                pass
            



# def set_initial_chars(string):
#     consonant = ''
#     vowel = ''
#     for i in range(len(string)):
#         if string[i].lower() in VOWELS and vowel == '':
#             vowel = string[i]
#         elif string[i].lower() not in VOWELS and consonant == '':
#             consonant = string[i]
        
#         if consonant != '' and vowel != '':
#             break
    
#     return consonant, vowel

if __name__ == '__main__':
    s = input()
    minion_game(s)
