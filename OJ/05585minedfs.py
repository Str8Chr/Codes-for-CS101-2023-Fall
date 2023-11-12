# using dfs to calculate the number of mines


def dfs(x, y, type):  # 深度优先搜索清除找到的晶矿
    # global m
    m[x][y] = '#'
    if x != n - 1 and m[x + 1][y] == type:
        dfs(x + 1, y, type)
    if y != n - 1 and m[x][y + 1] == type:
        dfs(x, y + 1, type)
    if x != 0 and m[x - 1][y] == type:
        dfs(x - 1, y, type)
    if y != 0 and m[x][y - 1] == type:
        dfs(x, y - 1, type)


k = int(input())
for _ in range(k):
    n = int(input())
    m = []
    for _ in range(n):
        m.append(list(input()))
    count_r = 0
    count_b = 0
    for i, j in [(i, j) for i in range(n) for j in range(n)]:
        if m[i][j] == 'r':
            dfs(i, j, 'r')
            count_r += 1
        if m[i][j] == 'b':
            dfs(i, j, 'b')
            count_b += 1
    print(count_r, count_b)
