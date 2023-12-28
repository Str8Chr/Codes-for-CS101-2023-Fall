n, x = map(int, input().split())
coins = sorted(list(map(int, input().split())))
dp = [[False, set()] for _ in range(x + 1)]; dp[0][0] = True
for i in range(n):
    for j in range(x-coins[i], -1, -1):
        if dp[j][0]:
            if not dp[j + coins[i]][0]:
                dp[j + coins[i]][0] = True
                dp[j + coins[i]][1].update(dp[j][1])
                dp[j + coins[i]][1].add(i)
            else: dp[j + coins[i]][1].intersection_update(dp[j][1])
print(len(dp[x][1])); print(*[coins[i] for i in sorted(dp[x][1])] if dp[x][0] else '')
