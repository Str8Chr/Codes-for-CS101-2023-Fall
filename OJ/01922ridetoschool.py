from math import ceil
while n := int(input()):
    print(ceil(min(16200 / x[0] + x[1] for _ in range(n) if (x := list(map(int, input().split())))[1] >= 0)))
