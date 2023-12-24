for _ in range(int(input())):
    n = int(input()); *prices, = map(int, input().split())
    dp = [(0, float('-inf')), (0, -prices[0]), (0, -prices[0])]
    for i in range(1, n):
        dp[1] = (max(dp[1][0], dp[1][1] + prices[i]), max(dp[0][0] - prices[i], dp[1][1]))
        dp[2] = (max(dp[2][0], dp[2][1] + prices[i]), max(dp[1][0] - prices[i], dp[2][1]))
    print(dp[2][0])
