input()
nums = list(map(int, input().split()))
nums.sort()
ans = 0
while len(nums) > 1:
    temp = nums.pop(0) + nums.pop(0)
    ans += temp
    for i in range(len(nums)):
        if temp < nums[i]:
            nums.insert(i, temp)
            break
    else:
        nums.append(temp)
print(ans)
