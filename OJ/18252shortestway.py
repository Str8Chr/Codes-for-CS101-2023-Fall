def spfa(s):
    dis = [float('inf') for _ in range(n)]
    dis[s] = 0
    queue = [s]
    cnt = [0] * n
    while queue:
        u = queue.pop(0)
        for v, w in G[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                if v not in queue:
                    queue.append(v)
                cnt[v] += 1
        if cnt[u] > n:
            return ['Error']
    return dis


# def dfs(s, t, visited, path, lenth):
#     if s == t:
#         path_lenths.append(lenth)
#         return
#     visited[s] = True
#     for i in range(n):
#         if G[s][i] != '' and not visited[i]:
#             path.append(i)
#             dfs(i, t, visited, path, lenth + G[s][i])
#             path.pop()
#     visited[s] = False
#
#
# def get_cycles(s, t, visited, lenth, dep):
#     if s == t and dep > 1:
#         cycle_lenths.append(lenth)
#         return
#     visited[s] = True
#     for i in range(t, n):
#         if G[s][i] != float('inf') and (
#                 not visited[i] or (i == t and dep > 1)):
#             get_cycles(i, t, visited, lenth + G[s][i], dep + 1)
#     visited[s] = False


for _ in range(int(input())):
    n, m, s = map(int, input().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        G[x - 1].append((y - 1, z))
    # cycle_lenths = []
    # for i in range(n):
    #     get_cycles(i, i, [False for _ in range(n)], 0, 1)
    # if any(i < 0 for i in cycle_lenths):
    #     print('Error')
    # else:
    print(*(i if i != float('inf') else 'null' for i in spfa(s - 1)))
