di = ((0, 1), (0, -1), (1, 0), (-1, 0))
ans = 0


def dfs(x, y):
    res = 0
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if matrix[nx][ny] < matrix[x][y]:
            if not length[nx][ny]: length[nx][ny] = dfs(nx, ny)
            res = max(res, length[nx][ny] + 1)
        else: res = max(res, 1)
    return res


r, c = map(int, input().split())
matrix = [[float('inf')] * (c+2)] +\
         [[float('inf')]+list(map(int, input().split()))+[float('inf')] for _ in range(r)] +\
         [[float('inf')] * (c+2)]
length = [[0] * (c+2) for _ in range(r+2)]
for i in range(1, r+1):
    for j in range(1, c+1):
        if not length[i][j]: length[i][j] = dfs(i, j)
        ans = max(ans, length[i][j])
print(ans)
