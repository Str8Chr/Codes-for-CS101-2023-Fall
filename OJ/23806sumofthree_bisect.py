from bisect import bisect_right
from collections import Counter
nums = sorted(list(map(int, input().split())))
c = Counter(nums)
i = cnt = 0
while i < len(nums) and nums[i] <= 0:
    r, d, prev = len(nums), c[nums[i]], float('inf')
    j = i + 1
    while j + 2 <= r:
        s = - nums[i] - nums[j]
        r = bisect_right(nums, s, j + 2, r)
        if nums[r - 1] == s:
            if nums[j] == prev:
                j += 1
                continue
            prev = nums[j]
            cnt += 1
        j += 1
    i += d
print(cnt)
