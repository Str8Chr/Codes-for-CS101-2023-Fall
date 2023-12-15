from collections import defaultdict
n, colors, same, streak = int(input()), defaultdict(int), {0}, 0
countColors = [n + 1] + [0] * n
*ribbons, = map(int, input().split())
for i in range(n):
    ribbon = ribbons[i]
    countColors[colors[ribbon]] -= 1
    if countColors[colors[ribbon]] == 0: same.remove(colors[ribbon])
    colors[ribbon] += 1
    countColors[colors[ribbon]] += 1
    same.add(colors[ribbon])
    if len(same) == 3:
        a, b, c = sorted(same)
        if b + 1 == c and countColors[c] == 1 or b == 1 and countColors[b] == 1: streak = i + 1
    elif len(same) == 2:
        a, b = sorted(same)
        if b == 1 or countColors[b] == 1: streak = i + 1
print(streak)
