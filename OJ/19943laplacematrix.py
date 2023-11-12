from collections import Counter
n, m = map(int, input().split())
adjacencyMatrix = [[0] * n for _ in range(n)]
degrees = []
for _ in range(m):
    u, v = map(int, input().split())
    adjacencyMatrix[u][v] = -1
    adjacencyMatrix[v][u] = -1
    degrees.append(u)
    degrees.append(v)
degrees = Counter(degrees)
for i in range(n):
    adjacencyMatrix[i][i] = degrees[i]
for i in range(n):
    print(*adjacencyMatrix[i])