# Note: Using stack can be more efficient
from collections import defaultdict
n = int(input())
colors = list(map(int, input().split()))
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
