from copy import deepcopy

di = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def update(x, y):
    cnt = 0
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            cnt += cells2[nx][ny]
    if cells2[x][y] == 1:
        if cnt < 2 or cnt > 3:
            cells[x][y] = 0
    else:
        if cnt == 3:
            cells[x][y] = 1


n, m = map(int, input().split())
cells = [list(map(int, input().split())) for _ in range(n)]
cells2 = deepcopy(cells)
for i in range(n):
    for j in range(m):
        update(i, j)
for i in range(n):
    print(*cells[i])