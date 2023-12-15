from itertools import combinations
from copy import deepcopy
di = ((0, 0), (0, -1), (1, 0), (-1, 0))


def flip(op):
    for c in range(2, n + 1):
        for r in range(1, m + 1):
            if (sum(op[r + dr][c - 1 + dc] for dr, dc in di) + board[r][c - 1]) % 2 == 1:
                op[r][c] = 1
    if all((sum(op[r + dr][n + dc] for dr, dc in di) + board[r][n]) % 2 == 0 for r in range(1, m + 1)):
        for r in range(1, m + 1):
            print(*op[r][1:-1])


m, n = 5, 6
board = [[0] * (n + 2)] + \
         [[0] + list(map(int, input().split())) + [0] for _ in range(m)] + \
         [[0] * (n + 2)]
op_ori = [[0] * (n + 2) for _ in range(m + 2)]
for i in range(m + 1):  # 枚举第一列的所有情形
    for manu in combinations(range(1, m + 1), i):
        operate = deepcopy(op_ori)
        for j in manu:
            operate[j][1] = 1
        flip(operate)
