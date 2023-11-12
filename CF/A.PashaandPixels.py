from collections import defaultdict


di = [(0, 1), (1, 0), (1, 1), (0, 0)]
n, m, k = map(int, input().split())
plan = defaultdict(lambda: float('inf'))
for i in range(k):
    x, y = map(int, input().split())
    plan[(x, y)] = min(plan[(x, y)], i)
ans = []
for x, y in plan.keys():
    if all((x + dx, y + dy) in plan.keys() for dx, dy in di):
        ans.append(max(plan[(x + dx, y + dy)] for dx, dy in di) + 1)
if ans:
    print(min(ans))
else:
    print(0)
