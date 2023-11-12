n, b = map(int, input().split())
value = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [0] * (b + 1)
for i in range(n):
    for j in range(b, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + value[i])
print(dp[b])