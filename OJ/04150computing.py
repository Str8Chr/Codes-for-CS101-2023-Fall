n = int(input())
abc = tuple(tuple(map(int, input().split())) for _ in range(3))
dp = [[[0 for j in range(2)] for k in range(2)] for i in range(n)]
dp[0][0][0] = abc[0][0]
dp[0][0][1] = abc[1][0]
dp[0][1][0] = -1
dp[0][1][1] = -1
for i in range(1, n):
    dp[i][0][0] = max(dp[i - 1][0][1], dp[i - 1][1][1]) + abc[0][i]
    dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][1]) + abc[1][i]
    dp[i][1][0] = max(dp[i - 1][0][0], dp[i - 1][1][0]) + abc[1][i]
    dp[i][1][1] = max(dp[i - 1][0][0], dp[i - 1][1][0]) + abc[2][i]
print(max(dp[n - 1][0][0], dp[n - 1][1][0]))
