from collections import Counter
n = int(input())
*a, = map(int, input().split())
if n == 1:
    print(a[0])
    exit()
weight = Counter(a)
a = sorted(weight.keys()) + [float('inf')]
dp = [[0, 0, 0] for i in range(len(a) - 1)] # 跟随左边删除，自己删除，跟随右边删除
dp[0] = [float('-inf'), a[0] * weight[a[0]],
         [float('-inf'), a[1] * weight[a[1]]][a[1] == a[0] + 1]]
for i in range(1, len(a) - 1):
    if a[i] == a[i - 1] + 1:
        dp[i][0] = dp[i - 1][1]
        dp[i][1] = dp[i - 1][2]
    else:
        dp[i][0] = float('-inf')
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + a[i] * weight[a[i]]
    if a[i + 1] == a[i] + 1:
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + a[i + 1] * weight[a[i + 1]]
    else:
        dp[i][2] = float('-inf')
print(max(dp[-1]))
