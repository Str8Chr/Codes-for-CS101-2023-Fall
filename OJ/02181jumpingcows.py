n = int(input())
*potions, = map(int, (input() for _ in range(n)))
dp = [0] * n  # [下一步增加， 下一步减少】
dp[0] = (0, potions[0])
for i in range(1, n):
    dp[i] = (max(dp[i - 1][0], dp[i - 1][1] - potions[i]), max(dp[i - 1][1], dp[i - 1][0] + potions[i]))
print(max(dp[-1]))
