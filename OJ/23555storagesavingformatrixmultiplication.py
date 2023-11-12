from collections import defaultdict


n, m1, m2 = map(int, input().split())
a = defaultdict(lambda: 0)
b = defaultdict(lambda: 0)
c = {}
for _ in range(m1):
    x, y, v = map(int, input().split())
    a[(x, y)] = v
for _ in range(m2):
    x, y, v = map(int, input().split())
    b[(x, y)] = v
nonzero = []
for x, y in a:
    for i in range(n):
        if b[(y, i)]:
            nonzero.append((x, i))
for x, y in nonzero:
    if v := sum(a[(x, i)] * b[(i, y)] for i in range(n)):
        c[(x, y)] = v
for (x, y), v in sorted(c.items()):
    print(x, y, v)