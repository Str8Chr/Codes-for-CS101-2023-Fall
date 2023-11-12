# 所有点坐标先写行后写列，注意坐标不是从0开始的


def get_seg():  # 找出所有空格
    column = []
    for x in range(w + 2):
        for i in range(h + 2):
            if board[i][x] == ' ':
                if column and (i - 1, x) in column[-1]:
                    column[-1].append((i, x))
                elif i != h + 1 and board[i + 1][x] == ' ':
                    column.append([(i, x)])
                elif board[i][x - 1] == board[i][x + 1] == 'X':
                    column.append([(i, x)])
    yield column
    row = []
    for y in range(h + 2):
        for i in range(w + 2):
            if board[y][i] == ' ':
                if row and (y, i - 1) in row[-1]:
                    row[-1].append((y, i))
                elif i != w + 1 and board[y][i + 1] == ' ':
                    row.append([(y, i)])
    yield row


def is_crossed(a, b):  # 判断两个线段是否有交集
    if any(i in a for i in b) and a != b:
        return 1
    return 0


def get_dis(point, seg):
    if point[0] == seg[0][0] == seg[-1][0]:
        return 1 if seg[0][1] - point[1] == 1 or point[1] - \
            seg[-1][1] == 1 else 0
    elif point[1] == seg[0][1] == seg[-1][1]:
        return 1 if seg[0][0] - point[0] == 1 or point[0] - \
            seg[-1][0] == 1 else 0
    elif any(i[0] == point[0] for i in seg):
        return 2 if abs(point[1] - seg[0][1]) == 1 else 0
    elif any(i[1] == point[1] for i in seg):
        return 2 if abs(point[0] - seg[0][0]) == 1 else 0
    else:
        return 0


def get_path(start, dep, path):
    if d := G[start][-1]:
        res.append(dep + d)
        return
    for i in range(len(G) - 2):
        if G[start][i] and i not in path:
            get_path(i, dep + G[-2][i], path + [i])


count = 0
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    count += 1
    board = [[' '] * (w + 2)] + \
            [[' '] + list(input()) + [' '] for _ in range(h)] + \
            [[' '] * (w + 2)]
    segs = get_seg()
    column = next(segs)
    row = next(segs)
    G = [[0] * (len(column) + len(row) + 2)
         for _ in range(len(column) + len(row) + 2)]
    for i in range(len(column)):
        for j in range(len(row)):
            G[i][j + len(column)] = G[j + len(column)][i] = \
                is_crossed(column[i], row[j])

    print('Board #{}:'.format(count))
    count2 = 0
    while True:
        start0, start1, final0, final1 = map(int, input().split())
        if start0 == start1 == final0 == final1 == 0:
            break
        G[-2][:-2] = [get_dis((start1, start0), i) for i in column + row]
        for i in range(len(G) - 2):
            G[i][-1] = get_dis((final1, final0), (column + row)[i])
        count2 += 1
        res = []
        for i in range(len(G) - 2):
            if G[-2][i]:
                get_path(i, G[-2][i], [i])
        if res:
            print('Pair {}: {} segments.'.format(count2, min(res)))
        else:
            print('Pair {}: impossible.'.format(count2))
