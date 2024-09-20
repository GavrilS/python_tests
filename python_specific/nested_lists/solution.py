def main(student_list):
    lowest_score = -158
    second_lowest = -158
    count = 0
    for score in student_list.keys():
        if count == 0:
            lowest_score = score
            count += 1
        elif count == 1:
            if lowest_score < score:
                second_lowest = score
                count += 1
                continue
            elif lowest_score == score:
                continue
            else:
                second_lowest = lowest_score
                lowest_score = score
                count += 1
                continue
        
        if score < lowest_score:
            second_lowest = lowest_score
            lowest_score = score
        elif score > lowest_score and score < second_lowest:
            second_lowest = score
    
    result = sorted(student_list[second_lowest])
    for student in result:
        print(student)


if __name__ == '__main__':
    student_list = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if student_list.get(score, None):
            student_list[score].append(name)
        else:
            student_list[score] = [name]
    
    main(student_list)
