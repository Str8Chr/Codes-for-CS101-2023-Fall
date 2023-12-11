for _ in range(int(input())):
    n = int(input())
    c = [0] * (n + 1)
    move = [True] * (n + 1)
    for x in map(int, input().split()):
        if x <= n: c[x] += 1
    if c[0] <= 1: print(0); continue
    min_before = float('inf')
    for i in range(n + 1):
        if c[i] >= min_before: move[i] = False
        elif c[i] == 0: break
        else: min_before = c[i]
    dp = [float('inf')] * i + [0]
    for j in range(i, -1, -1):
        if move[j]:
            for k in range(j, i + 1):
                if move[k]:
                    dp[j] = min(dp[j], dp[k] + k * (c[j] - 1) + j)
    print(dp[0])
