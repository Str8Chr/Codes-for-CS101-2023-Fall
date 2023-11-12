from heapq import heappush, heappop, heapify


n = int(input())
nums = list(map(int, input().split()))
heapify(nums)
ans = 0
for i in range(n - 1):
    temp = heappop(nums) + heappop(nums)
    ans += temp
    heappush(nums, temp)
print(ans)
