def dfs(word):
    if len(word) == 0:
        return True
    for i in range(4):
        if not used[i] and dic[word[0]][i]:
            used[i] = True
            if dfs(word[1:]):
                return True
            used[i] = False
    return False


n = int(input())
dic = {chr(i): [False] * 4 for i in range(65, 91)}
for i in range(4):
    for s in input(): dic[s][i] = True
for i in range(n):
    used = [False] * 4
    print('YES' if dfs(input()) else 'NO')
