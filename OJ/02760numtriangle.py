n = int(input())
triangle = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * n
dp[0] = triangle[0][0]
for i in range(1, n):
    dp[i] = dp[i - 1] + triangle[i][i]
    for j in range(i - 1, 0, -1):
        dp[j] = max(dp[j - 1], dp[j]) + triangle[i][j]
    dp[0] += triangle[i][0]
print(max(dp))