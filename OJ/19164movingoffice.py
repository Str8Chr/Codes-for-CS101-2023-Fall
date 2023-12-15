t, m = map(int, input().split()); Beijing, Nanjing, dp = [], [], [(0, 0)] + [None] * t
for _ in range(t): b, n = map(int, input().split()); Beijing.append(b); Nanjing.append(n)
for i in range(1, t + 1): dp[i] = (max(dp[i - 1][0] + Beijing[i - 1], dp[i - 1][1] - m + Beijing[i - 1]), max(dp[i - 1][0] - m + Nanjing[i - 1], dp[i - 1][1] + Nanjing[i - 1]))
print(max(dp[-1]))
