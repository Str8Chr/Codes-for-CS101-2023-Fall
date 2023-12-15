di = ((0, 1), (1, 0), (0, -1), (-1, 0))
ans = float('inf')


def dfs(x, y, dep=0):
    global ans
    if visited[x][y] or dep >= ans or matrix[x][y] == 2: return
    if matrix[x][y] == 1: ans = dep; return
    visited[x][y] = True
    for dx, dy in di:
        dfs(x + dx, y + dy, dep + 1)
    visited[x][y] = False


m, n = map(int, input().split())
matrix = [[2] * (n + 2)] + \
         [[2] + list(map(int, input().split())) + [2] for _ in range(m)] + \
         [[2] * (n + 2)]
visited = [[False] * (n + 2) for _ in range(m + 2)]
dfs(1, 1)
print(ans if ans != float('inf') else 'NO')