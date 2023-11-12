roses = input()
dp = [[0, 0] for i in range(len(roses))]  # all red, all blue
dp[0] = [roses[0] == 'B', roses[0] == 'R']
for i in range(1, len(roses)):
    if roses[i] == 'R':
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = min(dp[i - 1][1] + 1, dp[i - 1][0] + 1)
    else:
        dp[i][1] = dp[i - 1][1]
        dp[i][0] = min(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
print(dp[len(roses) - 1][0] + 0)
