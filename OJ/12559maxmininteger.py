def bubble_sort(n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[j] + nums[i] < nums[i] + nums[j]:
                nums[j], nums[i] = nums[i], nums[j]


n = int(input())
nums = input().split()
bubble_sort(n)
print(''.join(nums[::-1]), ''.join(nums))
