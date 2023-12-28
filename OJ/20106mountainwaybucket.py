# try to use dijkstra algorithm
# use bucket to optimize dijkstra algorithm, but not efficient
from collections import deque
di = ((1, 0), (-1, 0), (0, 1), (0, -1))

class Node:
    def __init__(self, value, cost): self.value, self.cost, self.visited = value, cost, False

def dijkstra(xs, ys, xe, ye):
    if mount[xs][ys] == '#' or mount[xe][ye] == '#': return float('inf')
    nodes = [[Node((i, j), float('inf')) for j in range(n + 2)] for i in range(m + 2)]
    nodes[xs][ys].cost = 0
    max_cost = 0
    buckets = [deque() for _ in range(1 << 15)]
    buckets[0].append(nodes[xs][ys])
    for cost in range(1 << 15):
        if cost > max_cost: break
        while buckets[cost]:
            node = buckets[cost].popleft(); x, y = node.value
            if x == xe and y == ye: return node.cost
            if nodes[x][y].visited: continue
            nodes[x][y].visited = True
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if mount[nx][ny].isdigit():
                    delta = abs(int(mount[nx][ny]) - int(mount[x][y]))
                    if node.cost + delta < nodes[nx][ny].cost:
                        nodes[nx][ny].cost = node.cost + delta
                        max_cost = max(max_cost, nodes[nx][ny].cost)
                        buckets[nodes[nx][ny].cost].append(nodes[nx][ny])
    return float('inf')

m, n, p = map(int, input().split())
mount = [['#'] * (n + 2)] + [['#'] + input().split() + ['#'] for _ in range(m)] + [['#'] * (n + 2)]
for _ in range(p): print(ans if (ans := dijkstra(*map(lambda x: int(x)+1, input().split()))) != float('inf') else 'NO')