class St:
    def __init__(self, v):
        self.v = v  # v for value, str

    def __lt__(self, other):
        return self.v + other.v < other.v + self.v


m, n = int(input()), int(input())
nums = sorted([St(x) for x in input().split()])
dp = [[False, ''] for _ in range(m + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(m, len(nums[i].v) - 1, -1):
        if dp[j - len(nums[i].v)][0]: dp[j] = [True, nums[i].v + dp[j - len(nums[i].v)][1]]
for i in range(m, -1, -1):
    if dp[i][0]: print(dp[i][1]); break
