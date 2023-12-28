from bisect import bisect_left
for _ in range(int(input())):
    n = int(input())
    stick = []; sticks = []
    for i, x in enumerate(input().split()):
        stick.append(int(x))
        if i % 2: sticks.append(tuple(stick)); stick = []
    sticks.sort()
    tails, ans = [0] * n, 0
    for stick in sticks:
        tails[bisect_left(tails, -stick[1])] = -stick[1]
        ans += tails[ans] != 0
    print(ans)
