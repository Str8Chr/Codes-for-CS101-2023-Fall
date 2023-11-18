t, m = map(int, input().split())
cost = []
value = []
for _ in range(m):
    c, v = map(int, input().split())
    cost.append(c)
    value.append(v)
dp = [0] * (t + 1)
for i in range(m):
    for j in range(t, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + value[i])
print(dp[t])