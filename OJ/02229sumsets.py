dp = [1] + [0] * int(input())
for i in range(1, len(dp)): dp[i] = (dp[i - 1] + (i + 1) % 2 * dp[i >> 1]) % (10 ** 9)
print(dp[-1])
