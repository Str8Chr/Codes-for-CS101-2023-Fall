from queue import Queue
di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(xs, ys, xf, yf):
    xs, ys, xf, yf = xs + 1, ys + 1, xf + 1, yf + 1
    if mount[xs][ys] == '#' or mount[xf][yf] == '#': return float('inf')
    queue = Queue()
    queue.put((xs, ys))
    dis = [[float('inf')] * (n + 2) for _ in range(m + 2)]
    dis[xs][ys] = 0
    while not queue.empty():
        x, y = queue.get()
        if x == xf and y == yf: continue
        for dx, dy in di:
            if mount[x + dx][y + dy].isdigit():
                delta = abs(int(mount[x + dx][y + dy]) - int(mount[x][y]))
                if dis[x][y] + delta < dis[x + dx][y + dy]:
                    dis[x + dx][y + dy] = dis[x][y] + delta
                    queue.put((x + dx, y + dy))
    return dis[xf][yf]


m, n, p = map(int, input().split())
mount = [['#'] * (n + 2)] + \
        [['#'] + input().split() + ['#'] for _ in range(m)] + \
        [['#'] * (n + 2)]
for _ in range(p):
    print(ans if (ans := bfs(*map(int, input().split()))) != float('inf') else 'NO')
