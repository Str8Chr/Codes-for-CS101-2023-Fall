from math import log2
n, *pieces = map(int, input().split())
pieces.sort()
for i in range(len(pieces) - 1, -1, -1):
    for j in range(i):
        if pieces[i] % pieces[j] == 0:
            del pieces[i]
            break
*pieces, = zip(pieces, [1] * len(pieces))
for i in range(len(pieces)):
    for j in range(1, int(log2(n / pieces[i][0])) + 1):
        pieces.append((pieces[i][0] * 2 ** j, 2 ** j))
dp = [0] + [float('-inf')] * n
for p in pieces:
    for i in range(n, p[0] - 1, -1):
        dp[i] = max(dp[i], dp[i - p[0]] + p[1])
print(dp[n])