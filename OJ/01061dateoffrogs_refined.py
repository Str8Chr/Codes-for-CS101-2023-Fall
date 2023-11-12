import math
def mul():
    for i in range(int(diff / f)):
        if (dist + i * l) % diff == 0: return dist + i * l
x, y, m, n, l = map(int, input().split()); dist, diff = ((x - y) % l, m - n) if m > n else ((y - x) % l, n - m); print(int(l / f - mul() / diff) if diff % (f := math.gcd(diff, l)) == 0 and diff else 'Impossible')