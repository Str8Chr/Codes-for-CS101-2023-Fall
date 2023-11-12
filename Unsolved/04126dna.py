from collections import defaultdict


def dfs(frag: str, lnt: int, dpt=1) -> None:
    global ans
    if dpt == n:
        ans = min(ans, lnt)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            if DNAs[i] in frag:
                dfs(frag, lnt, dpt + 1)
            else:
                for j in range(len(DNAs[i]) - 1, -1, -1):
                    if frag.endswith(DNAs[i][:j]):
                        dfs(frag + DNAs[i][j:], lnt + len(DNAs[i]) - j, dpt + 1)
                        break
            visited[i] = False


for _ in range(int(input())):
    n = int(input())
    DNAs = tuple(input() for _ in range(n))
    visited = defaultdict(bool)
    ans = 140
    for i in range(n):
        visited[i] = True
        dfs(DNAs[i], len(DNAs[i]))
        visited[i] = False
    print(ans)
