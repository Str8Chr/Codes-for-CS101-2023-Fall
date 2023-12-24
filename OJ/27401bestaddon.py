# a variant of the backpack problem
n, t = map(int, input().split())
*prices, = map(int, input().split())
s = sum(prices)
if s < t: print(0); exit()
dp = [True] + [False] * (t + max(prices))
for p in prices:
    for i in range(t, - 1, -1):
        if not dp[i + p]: dp[i + p] = dp[i]
print(t + dp[t:].index(True))
