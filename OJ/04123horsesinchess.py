dx = (1, 1, 2, 2, -1, -1, -2, -2)
dy = (2, -2, 1, -1, 2, -2, 1, -1)


def dfs(dep, x, y):
    if dep == n * m:
        global ans
        ans += 1
        return
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m and not board[tx][ty]:
            board[tx][ty] = True
            dfs(dep + 1, tx, ty)
            board[tx][ty] = False


for i in range(int(input())):
    n, m, x, y = map(int, input().split())
    board = [[False] * m for i in range(n)]
    ans = 0
    board[x][y] = True
    dfs(1, x, y)
    print(ans)
