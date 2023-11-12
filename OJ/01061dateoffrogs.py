import math


x, y, m, n, l = map(int, input().split())
if m > n:
    dist = (x - y) % l
    diff = m - n
else:
    dist = (y - x) % l
    diff = n - m
f = math.gcd(diff, l)
for i in range(int(diff / f)):
    multi = (dist + i * l)
    if multi % diff == 0:
        print(int(l / f - multi / diff))
        break
else:
    print('Impossible')
