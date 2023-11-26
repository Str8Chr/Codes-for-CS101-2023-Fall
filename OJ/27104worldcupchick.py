n, *a = int(input()), *map(int, input().split())
rang = sorted([(i + 1 - a[i], min(i + 1 + a[i], n)) for i in range(n)])
# m = 0
# toDel = []
# for i in range(n):
#     if rang[i][1] > m:
#         m = rang[i][1]
#     else:
#         toDel.append(i)
# for i in reversed(toDel):
#     del rang[i]
rang += [(n + 1, n + 1)]
cur = 1
camera = ans = max_right = 0
while cur <= n:
    if rang[camera][0] <= cur:
        max_right = max(rang[camera][1], max_right)
        camera += 1
    else:
        ans += 1
        cur = max_right + 1
print(ans)
