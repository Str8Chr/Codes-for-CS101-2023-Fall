import array
R, C = map(int, input().split()); N = int(input())
trod = [array.array("B", [0] * (C + 1)) for _ in range(R + 1)]
points = [tuple(map(int, input().split())) for _ in range(N)]
for x, y in points: trod[x][y] = 1
points.sort()
max_count = 2
for i in range(N):
    x1, y1 = points[i]
    for j in range(i + 1, N):
        x2, y2 = points[j]; dx, dy = x2 - x1, y2 - y1
        if 0 < x1-dx <= R and 0 < y1-dy <= C: continue
        if not (0 < x1 + dx * (max_count - 1) <= R): break
        if not (0 < y1 + dy * (max_count - 1) <= C): continue
        cnt = 2
        while 0 < x2 + dx <= R and 0 < y2 + dy <= C:
            x2 += dx; y2 += dy; cnt += 1
            if not trod[x2][y2]: break
        else: max_count = max(max_count, cnt)
print(max_count if max_count > 2 else 0)
