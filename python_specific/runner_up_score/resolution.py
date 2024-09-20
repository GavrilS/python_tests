def main(arr):
    top_score = 0
    second_best = 0
    populated_scores = 0
    for i in arr:
        if populated_scores > 1:
            top_score, second_best = check_for_new_score(top_score, second_best, i)
        else:
            if populated_scores == 0:
                top_score = i
                populated_scores += 1
                continue
            elif populated_scores == 1:
                if i > top_score:
                    second_best = top_score
                    top_score = i
                    populated_scores += 1
                    continue
                elif i == top_score:
                    continue
                else:
                    second_best = i
                    populated_scores += 1
                    continue
    
    print(second_best)


def check_for_new_score(top, second, current):
    if current > top:
        if top > second:
            second = top
        top = current
    elif current > second and current < top:
        second = current
    
    return top, second


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    main(arr)
