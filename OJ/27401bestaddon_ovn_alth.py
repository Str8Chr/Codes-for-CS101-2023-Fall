# O(VN) time
# but the test data doesn't contain same numbers of large numbers
from collections import Counter
n, t = map(int, input().split())
prices = Counter(map(int, input().split()))
if sum(map(lambda x: x[0] * x[1], prices.items())) < t: print(0); exit()
dp = [0] + [-1] * (t + max(prices))  # dp[i]表示前k个物品填满容量为i的背包时最后放的物品j剩下多少
for j in prices:
    for i in range(len(dp)):
        if dp[i] >= 0: dp[i] = prices[j]
    for i in range(len(dp) - j):
        if dp[i] > 0: dp[i + j] = max(dp[i + j], dp[i] - 1)
for i in range(t, len(dp)):
    if dp[i] >= 0: print(i); exit()
