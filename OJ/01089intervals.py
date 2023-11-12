def is_intersect(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


n = int(input())
inters = [list(map(int, input().split())) for _ in range(n)]
inters.sort(key=lambda x: x[0])
res = []
for i in inters:
    if res and is_intersect(res[-1], i):
        res[-1][1] = max(res[-1][1], i[1])
    else:
        res.append(i)
for i in res:
    print(*i)