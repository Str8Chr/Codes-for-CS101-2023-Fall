from heapq import heappop, heappush
from collections import defaultdict


class Node:

    def __init__(self, value, cost):
        self.value = value
        self.cost = cost
        self.visited = False
        self.path = str()

    def __lt__(self, other):
        return (self.cost, self.path) < (other.cost, other.path)


def dijkstra(s, e):
    nodes = defaultdict(lambda: Node(None, float('inf')))
    nodes[s] = Node(s, 0)
    queue = []; heappush(queue, Node(s, 0))
    while queue:
        node = heappop(queue)
        x = node.value
        if x == e: return node.cost, node.path
        if nodes[x].visited: continue
        nodes[x].visited = True
        nex = (x * 3, x // 2)
        for i in range(2):
            a = nex[i]
            if nodes[a].cost >= node.cost + 1:
                nodes[a].cost, nodes[a].path = node.cost + 1, node.path + ['H', 'O'][i]
                t = Node(a, nodes[a].cost); t.path = nodes[a].path
                heappush(queue, t)
    return float('inf')


while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    print(*dijkstra(n, m), sep='\n')
