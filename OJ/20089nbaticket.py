prices = [1, 2, 5, 10, 20, 50, 100]
money = int(input())
*tickets, = map(int, input().split())
if money % 50 != 0: print('Fail'); exit()
money //= 50
dp = [0] + [float('inf')] * money
for i in range(7):  # 每种票都在O(log(tickets[i]))的时间内处理完
    if prices[i] * tickets[i] >= money:  # 票的数量多到超过背包容量，转换成完全背包
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
