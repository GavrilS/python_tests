if __name__=='__main__':
    N = int(input())
    numbers = input().split()
    t = tuple(map(int, numbers))

    print(hash(t))
