from collections import defaultdict
from heapq import heappush, heappop
q = int(input())
l, r = [], []  # 维护l的最大值和r的最小值
left, right = defaultdict(int), defaultdict(int)
for _ in range(q):
    operation, a, b = input().split()
    a, b = int(a), int(b)
    if operation == '+': heappush(l, -a); heappush(r, b); left[a] += 1; right[b] += 1
    else: left[a] -= 1; right[b] -= 1
    while l and left[-l[0]] <= 0: heappop(l)
    while r and right[r[0]] <= 0: heappop(r)
    print('YES' if l and r and -l[0] > r[0] else 'NO')
