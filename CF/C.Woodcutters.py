trees = [[x, x - h, x + h] for x, h in
         [map(int, input().split()) for _ in range(int(input()))]]
trees.sort(key=lambda x: x[0])
trees = [[float('-inf')] * 3] + trees + [[float('inf')] * 3]
dp = [[0, 0] for i in range((len(trees) - 1))]
for i in range(1, len(trees) - 1):
    dp[i][0] = max(dp[i - 1][0] + 1 if trees[i][1] > trees[i - 1][0] else dp[i - 1][0],
                   dp[i - 1][1] + 1 if trees[i][1] > trees[i - 1][2] else dp[i - 1][1])
    if trees[i + 1][0] > trees[i][2]:
        dp[i][1] = max(dp[i - 1][0] + 1, dp[i - 1][1] + 1)
    else:
        dp[i][1] = dp[i - 1][1]
        trees[i][2] = trees[i][0]
print(max(dp[-1]))
