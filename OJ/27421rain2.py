from heapq import heappush, heappop
from itertools import product
m, n = map(int, input().split())
heightMap = [list(map(int, input().split())) for _ in range(m)]
heap, visited = [], [[False] * n for _ in range(m)]
for i, j in product(range(m), (0, n - 1)):
    heappush(heap, (heightMap[i][j], i, j))
    visited[i][j] = True
for i, j in product((0, m - 1), range(n)):
    heappush(heap, (heightMap[i][j], i, j))
    visited[i][j] = True
# 围成一圈，并逐步缩圈
result = 0
while heap:
    height, i, j = heappop(heap)
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= x < m and 0 <= y < n and not visited[x][y]:
            result += max(0, height - heightMap[x][y])
            heappush(heap, (max(heightMap[x][y], height), x, y))
            visited[x][y] = True
print(result)
