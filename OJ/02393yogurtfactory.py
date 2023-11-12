n, s = map(int, input().split())
C = [0] * n
Y = [0] * n
for i in range(n):
    C[i], Y[i] = map(int, input().split())
dp = [C[i] - C[i - 1] - s for i in range(1, n)]
dp.insert(0, 0)
for i in range(1, n):
    dp[i] = dp[i - 1] + dp[i] if dp[i - 1] > 0 and dp[i - 1] + \
        dp[i] > 0 else max(dp[i], 0)
print(sum([(C[i] - dp[i]) * Y[i] for i in range(n)]))