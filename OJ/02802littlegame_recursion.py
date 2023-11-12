from copy import deepcopy
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def search_path(start, final):  # 递归遍历。di是上一步的方向，如果这一步和上一步方向一样，cnt不变，否则加1
    queue = [(start, 0, -1)]
    board = deepcopy(board_original)
    while queue:
        (x, y), cnt, di = queue.pop(0)
        for i in range(4):
            if (x + direction[i][0], y + direction[i][1]) == final:
                res.append(cnt + (di != i))
            elif 0 <= x + direction[i][0] <= h + 1 and \
                    0 <= y + direction[i][1] <= w + 1 and \
                    board[x + direction[i][0]][y + direction[i][1]] == ' ':
                    board[x + direction[i][0]][y + direction[i][1]] = 'Y'
                    queue.append([(x + direction[i][0], y + direction[i][1]), cnt + (di != i), i])


count = 0
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    count += 1
    board_original = [[' '] * (w + 2)] + \
            [[' '] + list(input()) + [' '] for _ in range(h)] + \
            [[' '] * (w + 2)]  # 用空格把board包围起来
    print('Board #{}:'.format(count))
    count2 = 0
    while True:
        start0, start1, final0, final1 = map(int, input().split())
        if start0 == start1 == final0 == final1 == 0:
            print()
            break
        count2 += 1
        res = []
        search_path((start1, start0), (final1, final0))
        if res:
            print('Pair {}: {} segments.'.format(count2, min(res)))
        else:
            print('Pair {}: impossible.'.format(count2))
