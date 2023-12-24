m, n = map(int, input().split()); *out, = map(int, input().split()); *weight, = map(int, input().split())
mino = [m] * (n + 1); dp = [0] * (m + 1)
for i, o in enumerate(reversed(out)): mino[o] = m - i - 1
for o in range(1, n + 1):
    for i in range(mino[o], m): dp[i] = max(dp[i - 1] + (weight[i] * (out[i] == o)), dp[i])
print(dp[-2])
