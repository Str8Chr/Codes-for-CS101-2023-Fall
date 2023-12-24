from copy import deepcopy
ops = ((0, -1), (0, 1), (1, 0), (-1, 0))  # 左右下上


def dfs(board_inp, prev=-1, dep=0):
    if dep == p: ans.append(max([max(b) for b in board_inp])); return
    for k in range(4):
        if k == prev: continue
        board = deepcopy(board_inp); changed = True
        while changed:
            dx, dy = ops[k]; changed = False
            for i in cycle1[k]:
                for j in cycle2[k]:
                    if board[i][j] == 0: continue
                    if board[i + dx][j + dy] == 0:
                        board[i + dx][j + dy], board[i][j] = board[i][j], 0; changed = True
                    elif board[i + dx][j + dy] == board[i][j]:
                        board[i + dx][j + dy] *= 2; board[i][j] = 0; changed = True
        dfs(board, k, dep + 1)


m, n, p = map(int, input().split())
board_orig = [list(map(int, input().split())) for _ in range(m)]
cycle1 = [range(m), range(m), range(m - 1), range(m-1, 0, -1)]
cycle2 = [range(n-1, 0, -1), range(n - 1), range(n), range(n)]
ans = []
dfs(board_orig)
print(max(ans))
