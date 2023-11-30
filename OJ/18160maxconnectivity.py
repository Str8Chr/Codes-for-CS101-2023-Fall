di = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1))


def dfs(x, y):
    area = 1
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == 'W':
            board[nx][ny] = '.'
            area += dfs(nx, ny)
    return area


for _ in range(int(input())):
    n, m = map(int, input().split())
    board = ([['.'] * (m + 2)] +
             [['.'] + list(input()) + ['.'] for _ in range(n)] +
             [['.'] * (m + 2)])
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] == 'W':
                board[i][j] = '.'
                ans = max(ans, dfs(i, j))
    print(ans)