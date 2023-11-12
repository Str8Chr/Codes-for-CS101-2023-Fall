# Exhaust the first line, O(2^n)
from copy import deepcopy
d = [(0, 0), (0, 1), (0, -1), (1, 0)]


def flip(r, count, board):
    for c in range(4):
        if board[r - 1][c]:
            for dr, dc in d:
                if 0 <= r + dr < 4 and 0 <= c + dc < 4:
                    board[r + dr][c + dc] ^= 1
            count += 1
    if r < 3:
        flip(r + 1, count, board)
    elif not any(board[r]):
        ans.append(count)


def exhaust():
    for i in range(2 ** 4):
        cnt = 0
        board = deepcopy(board_original)
        for j in range(4):
            if i & (1 << j):
                board[0][j] ^= 1
                board[1][j] ^= 1
                if j > 0:
                    board[0][j - 1] ^= 1
                if j < 3:
                    board[0][j + 1] ^= 1
                cnt += 1
        flip(1, cnt, board)


board_original = [[0 if c == 'w' else 1 for c in input()] for _ in range(4)]
ans = []
exhaust()
for r in range(4):
    for c in range(4):
        board_original[r][c] ^= 1
exhaust()
print(min(ans, default='Impossible'))
