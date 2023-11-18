def dRow(r):
    cnt = 0
    cnt2 = 0
    ans = 0
    for c in range(m):
        if matrix[r][c] == 1:
            cnt += 1
            if matrix[r + 1][c] == 0:
                cnt2 += 1
            if matrix[r - 1][c] == 0:
                cnt2 += 1
        else:
            if cnt > 0:
                ans += 2
            cnt = 0
    else:
        if cnt > 0:
            ans += 2
    return ans + cnt2


n, m = map(int, input().split())
matrix = ([[0] * m] +
          [list(map(int, input().split())) for _ in range(n)]
          + [[0] * m])
print(sum(dRow(r) for r in range(1, n + 1)))