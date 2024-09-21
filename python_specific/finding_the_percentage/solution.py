def main(student_marks, student):
    score = 0
    for i in student_marks[student]:
        score += i
    
    print(float("{:.2f}".format(score/len(student_marks[student]))))


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    main(student_marks, query_name)
