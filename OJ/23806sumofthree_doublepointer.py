from collections import Counter
nums = sorted(list(map(int, input().split())))
c = Counter(nums)
i = cnt = 0
while i < len(nums) and nums[i] <= 0:
    l, r = i + 1, len(nums) - 1
    prev_l, prev_r = '', ''
    while l < r:
        if prev_l == nums[l]:
            l += 1
            continue
        if prev_r == nums[r]:
            r -= 1
            continue
        if nums[l] + nums[r] == -nums[i]:
            cnt += 1
            prev_l, prev_r = nums[l], nums[r]
        elif nums[l] + nums[r] < -nums[i]:
            prev_l = nums[l]
        else:
            prev_r = nums[r]
    i += c[nums[i]]
print(cnt)
