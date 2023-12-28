money, m = map(int, input().split())
*prices, = map(int, input().split())
*tickets, = map(int, input().split())
dp = [0] + [float('inf')] * money
for i in range(m):
    if prices[i] * tickets[i] >= money:
        for j in range(prices[i], money + 1):
            dp[j] = min(dp[j], dp[j - prices[i]] + 1)
    k = 1
    while k < tickets[i]:  # 二进制优化
        for j in range(money, prices[i] * k - 1, -1):  # 01背包
            dp[j] = min(dp[j], dp[j - prices[i] * k] + k)
        tickets[i] -= k
        k <<= 1
    for j in range(money, prices[i] * tickets[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - prices[i] * tickets[i]] + tickets[i])
print(dp[money] if dp[money] != float('inf') else 'Fail')
