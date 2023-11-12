n, m = map(int, input().split())
dp = [[1, 1] + [0] * (m - 1) for _ in range(n + 1)]
dp[0] = [1] * (m + 1)
dp[1] = [1, 1] + [2] * (m - 1)
for i in range(2, n + 1):
    for j in range(2, m + 1):
        if i < j:
            dp[i][j] = dp[i][i] + 1
        elif i == j:
            dp[i][j] = 2 ** i - 1
        else:
            dp[i][j] = dp[i - 1][j] * 2 - dp[i - j -1][j]
print(dp[n][m])
