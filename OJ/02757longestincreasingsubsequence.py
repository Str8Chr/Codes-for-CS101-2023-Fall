from bisect import bisect_left
n = int(input())
*seq, = map(int, input().split())
low = [float('-inf')] + [float('inf')] * (n + 1)
for x in seq: low[bisect_left(low, x)] = x
print(low.index(float('inf')) - 1)
