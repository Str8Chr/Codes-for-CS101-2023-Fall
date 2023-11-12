for _ in range(int(input())):
    maximum = int(input())
    minimum = 1
    permutation = list(map(int, input().split()))
    l = 0
    r = maximum - 1
    while l <= r:
        if permutation[l] == minimum:
            minimum += 1
            l += 1
        elif permutation[r] == minimum:
            minimum += 1
            r -= 1
        elif permutation[l] == maximum:
            maximum -= 1
            l += 1
        elif permutation[r] == maximum:
            maximum -= 1
            r -= 1
        else:
            break
    if l <= r:
        print(l + 1, r + 1)
    else:
        print(-1)