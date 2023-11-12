from queue import PriorityQueue as PQ


n = int(input())
nums = PQ()
for i in map(int, input().split()):
    nums.put(i)
ans = 0
for i in range(n - 1):
    temp = nums.get() + nums.get()
    ans += temp
    nums.put(temp)
print(ans)
