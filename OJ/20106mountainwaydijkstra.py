# try to use dijkstra algorithm
from heapq import heappush, heappop
di = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Node:
    def __init__(self, value, cost): self.value, self.cost, self.visited = value, cost, False
    def __lt__(self, other): return self.cost < other.cost


def dijkstra(xs, ys, xe, ye):
    if mount[xs][ys] == '#' or mount[xe][ye] == '#': return float('inf')
    nodes = [[Node((i, j), float('inf')) for j in range(n + 2)] for i in range(m + 2)]
    nodes[xs][ys].cost = 0
    queue = []; heappush(queue, Node((xs, ys), 0))
    while queue:
        node = heappop(queue); x, y = node.value
        if x == xe and y == ye: return node.cost
        if nodes[x][y].visited: continue
        nodes[x][y].visited = True  # 注意迪杰斯特拉算法的核心是每个节点只访问一次
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if mount[nx][ny].isdigit():
                delta = abs(int(mount[nx][ny]) - int(mount[x][y]))
                if node.cost + delta < nodes[nx][ny].cost:
                    nodes[nx][ny].cost = node.cost + delta
                    heappush(queue, Node((nx, ny), nodes[nx][ny].cost))
                    # 注意这里不能直接推入nodes[x][y]，否则queue中的对象会被修改导致乱序
    return float('inf')


m, n, p = map(int, input().split())
mount = [['#'] * (n + 2)] + [['#'] + input().split() + ['#'] for _ in range(m)] + [['#'] * (n + 2)]
for _ in range(p): print(ans if (ans := dijkstra(*map(lambda x: int(x)+1, input().split()))) != float('inf') else 'NO')