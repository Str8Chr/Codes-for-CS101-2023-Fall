from collections import defaultdict


n, m = map(int, input().split())
array = list(map(int, input().split()))
array_l = []
for i in range(m):
    array_l.append(int(input()))
not_in_right = defaultdict(lambda: 1)
dp = [0] * (n + 1)
dp[n] = 1
for l in range(n - 1, min(array_l) - 1, -1):
    not_in_right[array[l]] = 0
    dp[l] = dp[l + 1] + not_in_right[array[l - 1]]
for l in array_l:
    print(dp[l])