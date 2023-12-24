# a test data generator for OJ/27363
from random import randint, sample
from collections import defaultdict


def solve():
    colors = toFill
    colors_toFill = [0] * n
    color_positions = defaultdict(list)
    for i in range(n): color_positions[colors[i]].append(i)
    LandR = {(color_positions[color][0], color_positions[color][-1]):
             color for color in color_positions if color}
    ans = cnt = 0
    r_prev = float('inf')
    for l, r in sorted(LandR):
        if l > r_prev:
            ans, cnt, r_prev = max(ans, cnt), 1, r
        elif r <= r_prev:
            cnt, r_prev = cnt + 1, r
        else: print(-1); exit()
        colors_toFill[l:r + 1] = [LandR[(l, r)]] * (r - l + 1)
    if colors_toFill != colors: print(-1); exit()
    ans = max(ans, cnt)
    print(ans)


n = int(input('n: '))
k = int(input('k(增大k可以增大颜色数量): '))
toFill = [0] * n
number_of_colors = randint(k, n)
for color in sample(range(1, n + 1), number_of_colors):
    l = randint(0, n - 1)
    r = randint(l, n - 1)
    toFill[l:r + 1] = [color] * (r - l + 1)
print('Sample Input:')
print(n)
print(' '.join(map(str, toFill)))
print('Sample Output:')
solve()