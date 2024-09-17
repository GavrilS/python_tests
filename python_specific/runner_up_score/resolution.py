def main(arr):
    top_score = 0
    second_best = 0
    for i in arr:
        if i > top_score:
            if top_score > second_best:
                second_best = top_score
            top_score = i
        elif i > second_best and i < top_score:
            second_best = i
    
    print(second_best)



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    main(arr)
